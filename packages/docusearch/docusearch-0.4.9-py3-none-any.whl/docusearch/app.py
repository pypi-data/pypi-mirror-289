import warnings
import openai
import os
import faiss
import pdfplumber
import numpy as np
from docx import Document
import logging
import time
import tiktoken
import platform
import zipfile
from bs4 import BeautifulSoup
import ebooklib
from ebooklib import epub
from odf.opendocument import load
from odf.text import P
import json
import argparse
import importlib.metadata
import diskcache as dc
import markdown2
import subprocess
import webbrowser
from concurrent.futures import ThreadPoolExecutor, as_completed 

# Setup logging
logging.basicConfig(level=logging.INFO)
cache = dc.Cache(os.path.join(os.path.expanduser('~'), 'docusearch_cache'))
tokenizer = tiktoken.get_encoding('cl100k_base')

warnings.filterwarnings("ignore", category=UserWarning, module="ebooklib.epub")
warnings.filterwarnings("ignore", category=FutureWarning, module="ebooklib.epub")

def extract_text_from_pdf(pdf_path):
    text = ''
    try:
        with pdfplumber.open(pdf_path) as pdf:
            text = ''.join(page.extract_text() or '' for page in pdf.pages)
    except pdfplumber.pdfparser.PDFSyntaxError:
        logging.error(f"Error processing PDF file: {pdf_path}. The file is not a valid PDF.")
    return text

def extract_text_from_docx(docx_path):
    return '\n'.join([para.text for para in Document(docx_path).paragraphs])

def extract_text_from_txt(txt_path):
    with open(txt_path, 'r', encoding='utf-8') as file:
        return file.read()

def extract_text_from_odt(odt_path):
    doc = load(odt_path)
    text_content = []
    paragraphs = doc.getElementsByType(P)
    for paragraph in paragraphs:
        for node in paragraph.childNodes:
            if node.nodeType == 3:  # Text node
                text_content.append(node.data)
            elif node.nodeType == 1 and node.firstChild and node.firstChild.nodeType == 3:  # Element node with a Text node child
                text_content.append(node.firstChild.data)
    return '\n'.join(text_content)

def extract_text_from_html_zip(zip_path):
    text = ''
    with zipfile.ZipFile(zip_path, 'r') as z:
        for filename in z.namelist():
            if filename.endswith('.html'):
                with z.open(filename) as f:
                    text += BeautifulSoup(f, 'html.parser').get_text() + '\n'
    return text

def extract_text_from_epub(epub_path):
    book = epub.read_epub(epub_path)
    return '\n'.join(BeautifulSoup(item.get_body_content(), 'html.parser').get_text() + '\n' for item in book.get_items() if item.get_type() == ebooklib.ITEM_DOCUMENT)

def split_text_into_chunks(text, max_tokens):
    tokens = tokenizer.encode(text)
    return [tokenizer.decode(tokens[i:i + max_tokens]) for i in range(0, len(tokens), max_tokens)]

def generate_embeddings(text, api_key, model="text-embedding-ada-002"):
    openai.api_key = api_key
    chunks = split_text_into_chunks(text, max_tokens=2048)
    embeddings = [openai.Embedding.create(input=chunk, model=model)['data'][0]['embedding'] for chunk in chunks]
    return np.mean(embeddings, axis=0)

def get_new_files(directory, cached_files):
    return set(os.listdir(directory)) - cached_files

def read_documents(directory, api_key):
    documents, metadatas, ids, embeddings, unsupported_files = [], [], [], [], []
    if directory in cache:
        logging.info(f"Loading documents from cache for directory: {directory}")
        cached_data = cache[directory]
        cached_files = set(metadata["source"] for metadata in cached_data["metadatas"])
        new_files = get_new_files(directory, cached_files)

        if not new_files:
            return cached_data["documents"], cached_data["metadatas"], cached_data["ids"], cached_data["embeddings"], unsupported_files

        documents, metadatas, ids, embeddings = cached_data["documents"], cached_data["metadatas"], cached_data["ids"], list(cached_data["embeddings"])
    else:
        logging.info(f"Processing documents in directory: {directory}")
        new_files = set(os.listdir(directory))

    extractors = {
        ".pdf": extract_text_from_pdf,
        ".docx": extract_text_from_docx,
        ".txt": extract_text_from_txt,
        ".odt": extract_text_from_odt,
        ".zip": extract_text_from_html_zip,
        ".epub": extract_text_from_epub,
    }

    for filename in new_files:
        ext = os.path.splitext(filename)[1].lower()
        extractor = extractors.get(ext)
        if not extractor:
            unsupported_files.append(filename)
            continue

        text = extractor(os.path.join(directory, filename))
        if not text:
            logging.warning(f"Skipped empty or invalid file: {os.path.join(directory, filename)}")
            continue

        documents.append(text)
        metadata = {"source": filename}
        metadatas.append(metadata)
        doc_id = os.path.splitext(filename)[0]
        ids.append(doc_id)

        document_embedding = generate_embeddings(text, api_key)
        if document_embedding is None:
            return None, None, None, None, unsupported_files
        embeddings.append(document_embedding)

    embeddings = np.array(embeddings)
    cache[directory] = {"documents": documents, "metadatas": metadatas, "ids": ids, "embeddings": embeddings}

    return documents, metadatas, ids, embeddings, unsupported_files

def clear_cache():
    cache.clear()
    logging.info("Cache cleared successfully.")

def split_document(document, max_tokens=4096):
    return split_text_into_chunks(document, max_tokens=max_tokens)

def query_chunk(chunk_num, chunk, question, api_key, model="gpt-4", short_response=False, document_type="default"):
    openai.api_key = api_key
    max_completion_tokens = 512 if not short_response else 128
    max_input_tokens = 8192 - max_completion_tokens
    chunk = split_text_into_chunks(chunk, max_input_tokens)[0]
#Provide a detailed answer in tabular format and cite sentences from the document. Make sure your response is extremely well structured so I can parse the text, identify potential table structures, and then organize the data into a spreadsheet form.
    if document_type == "financial":
        prompt = f"Document chunk {chunk_num}:\n{chunk}\n\nQuestion: {question}\n\nProvide a detailed answer in tabular format and cite sentences from the document. Make sure your response is extremely well structured so I can parse the text, identify potential table structures, and then organize the data into a spreadsheet form." if not short_response else f"Document chunk {chunk_num}:\n{chunk}\n\nQuestion: {question}\n\nProvide a concise answer in tabular format and cite sentences from the document. Have a good mix of narration vs. tabular data. If something can be put in tabular format, put it in tabular format"
    else:
        prompt = f"Document chunk {chunk_num}:\n{chunk}\n\nQuestion: {question}\n\nProvide a detailed answer and cite sentences from the document. Make your response pretty using bolding, lists, italics, etc." if not short_response else f"Document chunk {chunk_num}:\n{chunk}\n\nQuestion: {question}\n\nProvide a concise answer and cite sentences from the document. Make your response pretty using bolding, lists, italics, etc."

    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=max_completion_tokens
    )
    return chunk_num, response.choices[0].message['content']

def get_answers_with_citations(question, document_chunks, api_key, model="gpt-4", short_response=False, document_type="default"):
    all_evidence = []

    def process_chunk(i, chunk):
        return query_chunk(i+1, chunk, question, api_key, model, short_response, document_type)

    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(process_chunk, i, chunk) for i, chunk in enumerate(document_chunks)]
        for future in as_completed(futures):
            chunk_num, answer = future.result()
            all_evidence.append((chunk_num, answer))

    return all_evidence

def combine_answers_with_citations(evidence_list):
    combined_answer = ""
    citations = []
    for chunk_num, answer in evidence_list:
        combined_answer += f"\n{answer}"
        sentences = [sent.strip() for sent in answer.split('.') if any(word in sent for word in answer.split())]
        citations.extend(sentences)
    return combined_answer, citations

def query_index(query_embedding, index, metadatas, documents, embeddings, heat="temperate", n_results=1, roaming=False):
    heat_levels = {"frostbite": 0.1, "glacial": 0.2, "artic": 0.3, "chill": 0.4, "temperate": 0.5, "warmth": 0.6, "blaze": 0.7, "scorch": 0.8, "inferno": 0.9, "supernova": 1.0, "docusearch": 1.1}
    
    if heat.lower() == "docusearch":
        raise ValueError("Whoa there. Docusearch is too hot to use as a parameter, try something a little more chill.")
    
    relevancy_threshold = heat_levels.get(heat.lower(), 0.5)
    
    query_embedding = np.array([query_embedding]).astype('float32')
    distances, indices = index.search(query_embedding, n_results)

    if roaming: 
        results = []
        
        for i in range(len(distances[0])):
            if distances[0][i] < relevancy_threshold:
                results.append({'distance': distances[0][i], 'metadata': metadatas[indices[0][i]], 'document': documents[indices[0][i]], 'embedding': embeddings[indices[0][i]]}) 
        return results
    else: 
        return [{'distance': distances[0][i], 'metadata': metadatas[indices[0][i]], 'document': documents[indices[0][i]], 'embedding': embeddings[indices[0][i]]} for i in range(n_results)]

def create_faiss_index(embeddings, embedding_dim):
    if embeddings.shape[0] < 256:
        index = faiss.IndexFlatL2(embedding_dim)
    else:
        nlist = max(1, min(100, embeddings.shape[0] // 4))
        quantizer = faiss.IndexFlatL2(embedding_dim)
        index = faiss.IndexIVFPQ(quantizer, embedding_dim, nlist, 8, 8)
        index.train(embeddings)
    index.add(embeddings)
    return index

def normalize_folder_path(folder_path):
    user_os = platform.system().lower()
    if 'windows' in user_os:
        return folder_path.replace('/mnt/c', 'C:').replace('/', '\\') if folder_path.startswith('/mnt/c') else folder_path
    return folder_path.replace('C:', '/mnt/c').replace('\\', '/') if folder_path[1] == ':' else folder_path.replace('\\', '/')

def identify_relevant_chunks(query_text, document_chunks, api_key, model="gpt-4"):
    relevant_chunks = []

    def process_chunk(chunk_num, chunk):
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"Document chunk {chunk_num}:\n{chunk}\n\nQuestion: Does this chunk contain any information relevant to the question: {query_text}?\n\nAnswer 'yes' if this chunk contains relevant information, otherwise answer 'no'. If there is even a single phrase that may be relevant, mark the chunk as 'yes'."}
            ],
            max_tokens=5
        )
        return chunk_num, response.choices[0].message['content'].strip().lower()

    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(process_chunk, i+1, chunk) for i, chunk in enumerate(document_chunks)]
        for future in as_completed(futures):
            chunk_num, answer = future.result()
            if answer == "yes":
                #print(f"Chunk {chunk_num} is relevant")
                relevant_chunks.append((chunk_num, document_chunks[chunk_num - 1]))
    return relevant_chunks

def process_best_matching_documents(query_text, api_key, folder_path, model="gpt-4", short_response=False, document_type="default", num_documents=1, heat="temperate", roaming=False):
    folder_path = normalize_folder_path(folder_path)
    start_time = time.time()
    documents, metadatas, ids, embeddings, unsupported_files = read_documents(folder_path, api_key)
    if documents is None:
        return None, None, unsupported_files
    processing_time = time.time() - start_time
    logging.info(f"Document processing time: {processing_time:.2f} seconds")

    embedding_dim = embeddings.shape[1]
    index = create_faiss_index(np.array(embeddings).astype('float32'), embedding_dim)

    query_embedding_start_time = time.time()
    query_embedding = generate_embeddings(query_text, api_key)
    if query_embedding is None:
        return None, None, unsupported_files
    query_embedding_time = time.time() - query_embedding_start_time
    logging.info(f"Embedding generation time: {query_embedding_time:.2f} seconds")

    if roaming:
        results = query_index(query_embedding, index, metadatas, documents, embeddings, heat, n_results=len(documents))
    else:
        results = query_index(query_embedding, index, metadatas, documents, embeddings, heat, n_results=num_documents)

    all_answers = []
    best_metadata = []

    def process_document(result):
        best_document = result['document']
        metadata = result['metadata']['source']

        filter_chunks_start_time = time.time()
        document_chunks = split_document(best_document)
        relevant_chunks = identify_relevant_chunks(query_text, document_chunks, api_key, model)
        filter_chunks_query_time = time.time() - filter_chunks_start_time
        #logging.info(f"Filter chunks time for document {metadata}: {filter_chunks_query_time:.2f} seconds")

        gpt_response_start_time = time.time()
        evidence_list = get_answers_with_citations(query_text, [chunk for _, chunk in relevant_chunks], api_key, model, short_response, document_type)
        gpt_response_time = time.time() - gpt_response_start_time
        logging.info(f"GPT response generation time for document {metadata}: {gpt_response_time:.2f} seconds")

        answer, citations = combine_answers_with_citations(evidence_list)
        return metadata, answer

    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(process_document, result) for result in results]
        for future in as_completed(futures):
            metadata, answer = future.result()
            if answer:
                best_metadata.append(metadata)
                all_answers.append(answer)

    querying_time = time.time() - start_time
    logging.info(f"Total querying time: {querying_time:.2f} seconds")

    return best_metadata, all_answers, unsupported_files

def process_query(query_text, api_key, folder_path,num_documents=1, heat="temperate", roaming=False, model="gpt-4", short_response=False, document_type="default", save_to_json=True):
    if not query_text or not api_key or not folder_path:
        raise ValueError("Query text, API key, and folder path are required")

    folder_path = normalize_folder_path(folder_path)
    if not os.path.exists(folder_path):
        logging.error(f"The folder path does not exist: {folder_path}")
        raise FileNotFoundError(f"The folder path does not exist: {folder_path}")

    best_metadata, answers, unsupported_files = process_best_matching_documents(query_text, api_key, folder_path, model, short_response, document_type, num_documents, heat, roaming)
    if best_metadata is None:
        raise ValueError("Invalid API key")

    response = {"document_sources": best_metadata, "answers": answers}
    if unsupported_files:
        response["warning"] = f"The following files are unsupported and were not processed: {', '.join(unsupported_files)}"

    if save_to_json:
        with open("data.json", "w") as json_file:
            json.dump(response, json_file)

    return best_metadata, answers, unsupported_files

def open_in_browser(query, follow_up_answer=None, json_file_path="data.json", wsl=False):
    output_file_path = "output.html"

    with open(json_file_path, "r") as json_file:
        saved_data = json.load(json_file)

    document_sources = saved_data.get("document_sources", [])
    answers = saved_data.get("answers", [])

    if follow_up_answer:
        follow_up_section = f"""
        <div class="follow-up-section">
            <h2>Follow-Up Answer:</h2>
            <div class="answer-header">
                <button class="toggle-button" onclick="toggleAnswer('follow-up-answer')">▼</button>
                <h3>Answer:</h3>
            </div>
            <div id="follow-up-answer" class="answer-content show">
                {markdown2.markdown(follow_up_answer, extras=["tables"])}

                <div class="follow-up-message">
            <h4>The previous answer has been provided below</h4>
           
        </div>
            </div>
             <hr style="border: 1px solid #eee;">
        </div>
        
        """
    else:
        follow_up_section = ""

    document_sections = "".join(
        f"""
        <div class="document-section">
            <h2>{document}</h2>
            <div class="answer-header">
                <button class="toggle-button" onclick="toggleAnswer('answer-{idx}')">▼</button>
                <h3>Answer:</h3>
            </div>
            <div id="answer-{idx}" class="answer-content show">
                {markdown2.markdown(answer, extras=["tables"])}
            </div>
        </div>
        """
        for idx, (document, answer) in enumerate(zip(document_sources, answers))
    )

    

    def split_text_into_lines(text, max_chars_per_line=68):
        words, lines, current_line = text.split(), [], ""
        for word in words:
            if len(current_line) + len(word) + 1 > max_chars_per_line:
                lines.append(current_line)
                current_line = word
            else:
                current_line += (" " if current_line else "") + word
        if current_line:
            lines.append(current_line)
        return lines

    query_html = "<br>".join(
        f'<span class="query-line" id="query-line-{idx}">{line}</span>'
        for idx, line in enumerate(split_text_into_lines(query))
    )

    html_with_style = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Query Result</title>
        <style>
            body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f5f5f5; margin: 20px; line-height: 1.6; color: #333; }}
            h1, h2, h3, h4, h5, h6 {{ color: #0b736e; }}
            table {{ width: 100%; border-collapse: collapse; margin-bottom: 20px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); }}
            th, td {{ border: 1px solid #ddd; padding: 12px; text-align: left; }}
            th {{ background-color: #0b736e; color: white; }}
            tr:nth-child(even) {{ background-color: #f2f2f2; }}
            tr:hover {{ background-color: #ddd; }}
            code {{ background-color: #f4f4f4; padding: 2px 4px; border-radius: 4px; color: #c7254e; }}
            pre {{ background-color: #f4f4f4; padding: 10px; border-radius: 4px; overflow-x: auto; color: #c7254e; }}
            .container {{ max-width: 800px; margin: auto; background: white; padding: 20px; border-radius: 8px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); }}
            a {{ color: #4CAF50; text-decoration: none; }}
            a:hover {{ text-decoration: underline; }}
            .document-section {{ margin-bottom: 40px; border-bottom: 1px solid #ddd; padding-bottom: 20px; }}
            .answer-header {{ display: flex; align-items: center; }}
            .answer-header h3 {{ margin: 0; margin-left: 10px; }}
            button {{ background: none; color: #0b736e; border: none; padding: 10px; cursor: pointer; font-size: 16px; width: 30px; text-align: center; }}
            button:hover {{ color: #094d4a; }}
            .answer-content {{ max-height: none; overflow: hidden; transition: max-height 0.3s ease-out, padding 0.3s ease-out; padding: 10px 0; }}
            .query-heading {{ font-size: 24px; font-weight: bold; color: #094d4a; margin-bottom: 20px; border-bottom: 1px solid #eee; padding-bottom: 10px;}}
            .typewriter span {{ display: inline-block; opacity: 0; }}
            .follow-up-section {{ margin-top: 40px; }}
        </style>
        <script>
            function toggleAnswer(id) {{
                var element = document.getElementById(id);
                var button = element.previousElementSibling.querySelector('.toggle-button');
                if (element.classList.contains('show')) {{
                    element.classList.remove('show');
                    element.style.maxHeight = "0";
                    element.style.padding = "0";
                    button.textContent = "▶";
                }} else {{
                    element.classList.add('show');
                    element.style.maxHeight = "none";
                    element.style.padding = "10px 0 10px 0";
                    button.textContent = "▼";
                }}
            }}

            function typeWriter(lineIndex) {{
                if (lineIndex >= {len(query_html.split("<br>"))}) return;
                const line = document.getElementById('query-line-' + lineIndex);
                const text = line.textContent;
                line.textContent = '';
                line.style.opacity = 1;
                let i = 0;
                const speed = 33;
                function type() {{
                    if (i < text.length) {{
                        line.textContent += text.charAt(i);
                        i++;
                        setTimeout(type, speed);
                    }} else if (lineIndex < {len(query_html.split("<br>")) - 1}) {{
                        typeWriter(lineIndex + 1);
                    }}
                }}
                type();
            }}

            window.onload = function() {{
                typeWriter(0);
            }};
        </script>
    </head>
    <body>
        <div class="container">
            <h1 class="query-heading typewriter">{query_html}</h1>
            {follow_up_section}
            {document_sections}
        </div>
    </body>
    </html>
    """

    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(html_with_style)
    open_file_in_browser(output_file_path, wsl)
    logging.info(f"HTML file created and opened: {output_file_path}")

def open_file_in_browser(file_path, wsl=False):
    user_os = platform.system().lower()
    if wsl:
        windows_path = os.path.abspath(file_path).replace('/mnt/c', 'C:').replace('/', '\\')
        subprocess.run(['explorer.exe', windows_path])
        return

    if 'windows' in user_os:
        webbrowser.open('file://' + os.path.realpath(file_path))
    elif 'darwin' in user_os:
        subprocess.run(['open', file_path])
    else:
        subprocess.run(['xdg-open', file_path])

def get_answer_from_context(context, api_key=os.getenv("OPENAI_API_KEY"), model="gpt-4", short_response=False, document_type="default"):
    openai.api_key = api_key
    max_completion_tokens = 512 if not short_response else 128

    if document_type == "financial":
        prompt = f"{context}\n\nProvide a detailed answer in tabular format and cite sentences from the previous answer. Make sure your response is extremely well structured so I can parse the text, identify potential table structures, and then organize the data into a spreadsheet form" if not short_response else f"{context}\n\nProvide a concise answer in tabular format and cite sentences from the previous answer. Make sure your response is extremely well structured so I can parse the text, identify potential table structures, and then organize the data into a spreadsheet form."
    else:
        prompt = f"{context}\n\nProvide a detailed answer and cite sentences from the previous answer. Make your response pretty using bolding, lists, italics, etc." if not short_response else f"{context}\n\nProvide a concise answer and cite sentences from the previous answer. Make your response pretty using bolding, lists, italics, etc."

    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=max_completion_tokens
    )
    return response.choices[0].message['content']

def read_single_document(directory, document_name):
    file_path = os.path.join(directory, document_name)

      # Check if the document is in the cache
    if directory in cache:
        cached_data = cache[directory]
        for metadata, doc in zip(cached_data["metadatas"], cached_data["documents"]):
            if metadata["source"] == document_name:
                logging.info(f"Loaded document from cache: {document_name}")
                return doc, None
            
    if not os.path.exists(file_path):
        logging.error(f"File not found: {file_path}")
        return None, f"File not found: {file_path}"

    extractors = {
        ".pdf": extract_text_from_pdf,
        ".docx": extract_text_from_docx,
        ".txt": extract_text_from_txt,
        ".odt": extract_text_from_odt,
        ".zip": extract_text_from_html_zip,
        ".epub": extract_text_from_epub,
    }

    ext = os.path.splitext(document_name)[1].lower()
    extractor = extractors.get(ext)
    if not extractor:
        logging.error(f"Unsupported file format: {document_name}")
        return None, f"Unsupported file format: {document_name}"

    text = extractor(file_path)
    if not text:
        logging.warning(f"Skipped empty or invalid file: {file_path}")
        return None, f"Skipped empty or invalid file: {file_path}"

    return text, None

# Function to follow up based on multiple documents
def follow_up(follow_up_question, api_key=os.getenv("OPENAI_API_KEY"), json_file_path="data.json", model="gpt-4", short_response=False, document_type="default", folder_path=None):
    follow_up_start_time = time.time()

    with open(json_file_path, "r") as json_file:
        saved_data = json.load(json_file)

    document_sources = saved_data["document_sources"]
    previous_answers = saved_data["answers"]
    context = f"Previous answers:" + "\n\n".join(previous_answers) + f"\n\nFollow-up question: {follow_up_question}"

    all_document_texts = []

    if folder_path:
        folder_path = normalize_folder_path(folder_path)

        for document_source in document_sources:
            single_start_time = time.time()
            document_text, error = read_single_document(folder_path, document_source)
            single_time = time.time() - single_start_time
            logging.info(f"Document processing time for {document_source}: {single_time:.2f} seconds")

            if document_text:
                all_document_texts.append(document_text)
        
        # Update context to include the text of all documents
        context += "\n\nHere are the documents as context \n\n".join(all_document_texts)
        
    gpt_response_start_time = time.time()
    answer = get_answer_from_context(context, api_key, model, short_response, document_type)
    gpt_response_time = time.time() - gpt_response_start_time
    logging.info(f"GPT response generation time: {gpt_response_time:.2f} seconds")

    follow_up_query_time = time.time() - follow_up_start_time
    logging.info(f"Follow-up query time: {follow_up_query_time:.2f} seconds")

    return answer

def main():
    parser = argparse.ArgumentParser(description='Docusearch Command Line Interface')
    parser.add_argument('--version', action='store_true', help='Show the version of docusearch')
    parser.add_argument('--clear-cache', action='store_true', help='Clear cache of documents')
    args = parser.parse_args()

    if args.version:
        version = importlib.metadata.version('docusearch')
        print(f"Docusearch {version}")

if __name__ == '__main__':
    main()
