from extractor.table_extractor import parallel_extract
from extractor.cleaner import convert_to_dataframe
import time

file_path = "input_pdfs/ais_sample.pdf"

if __name__ == "__main__":

    start = time.time()

    tables = parallel_extract(file_path)

    df = convert_to_dataframe(tables)

    end = time.time()

    print("Extraction Time:", end - start)

    print("\nPreview Data:")
    print(df.head())

    output_file = "extracted_output.xlsx"

    df.to_excel(output_file, index=False)

    print("\nExcel file created:", output_file)