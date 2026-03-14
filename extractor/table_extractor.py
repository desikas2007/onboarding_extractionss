import pdfplumber
from multiprocessing import Pool


def process_page(args):
    file_path, page_number = args

    with pdfplumber.open(file_path) as pdf:
        page = pdf.pages[page_number]
        tables = page.extract_tables()

    return tables


def parallel_extract(file_path):

    with pdfplumber.open(file_path) as pdf:
        page_count = len(pdf.pages)

    tasks = [(file_path, i) for i in range(page_count)]

    with Pool() as pool:
        results = pool.map(process_page, tasks)

    return results