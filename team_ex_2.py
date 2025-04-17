import wikipedia
import time
import os
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

os.makedirs("wiki_dl", exist_ok=True)

user_input = input("Enter a search term: ")
search_term = user_input if len(user_input) >= 4 else "generative artificial intelligence"

def convert_to_str(refs):
    return [str(r) for r in refs]

def download_and_save(topic):
    try:
        page = wikipedia.page(topic, auto_suggest=False)
        title = page.title
        references = convert_to_str(page.references)

        with open(f"wiki_dl/{title}.txt", "w", encoding="utf-8") as f:
            for ref in references:
                f.write(ref + "\n")
    except Exception as e:
        print(f"Couldn’t process '{topic}': {e}")

def wiki_sequentially(term):
    start = time.perf_counter()
    topics = wikipedia.search(term)
    for topic in topics:
        download_and_save(topic)
    end = time.perf_counter()
    print(f"Sequential finished in {end - start:.2f} seconds")

def concurrent_threads(term):
    start = time.perf_counter()
    topics = wikipedia.search(term)
    with ThreadPoolExecutor() as executor:
        executor.map(download_and_save, topics)
    end = time.perf_counter()
    print(f"Threaded finished in {end - start:.2f} seconds")

def dl_and_save_process(topic):
    download_and_save(topic)

def concurrent_process(term):
    start = time.perf_counter()
    topics = wikipedia.search(term)
    with ProcessPoolExecutor() as executor:
        executor.map(dl_and_save_process, topics)
    end = time.perf_counter()
    print(f"Multiprocessing finished in {end - start:.2f} seconds")

wiki_sequentially(search_term)
concurrent_threads(search_term)
concurrent_process(search_term)

