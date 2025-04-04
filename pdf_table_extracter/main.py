import os
import concurrent.futures
from tqdm import tqdm
from extractor import extract_words_from_pdf, group_words_to_rows, extract_table_from_rows
from utils import save_table

input_dir = "samples/input/"
output_dir = "samples/output/"
file_format = "xlsx"  # Change to "csv" if needed

# Ensure output directory exists
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def process_pdf(file):
    """Processes a single PDF and extracts tables."""
    pdf_path = os.path.join(input_dir, file)
    pages = extract_words_from_pdf(pdf_path)

    for page_num, words in enumerate(pages):
        grouped = group_words_to_rows(words)
        table = extract_table_from_rows(grouped)

        output_file = os.path.join(output_dir, f"{file.replace('.pdf', '')}_page_{page_num + 1}.{file_format}")
        save_table(table, output_file, file_format)

    return file  # Return file name when done

input_files = [f for f in os.listdir(input_dir) if f.endswith(".pdf")]

# Multi-threaded PDF processing
with concurrent.futures.ThreadPoolExecutor() as executor:
    results = list(tqdm(executor.map(process_pdf, input_files), total=len(input_files), desc="Processing PDFs", unit="file"))

print("\n✅ All PDFs processed successfully!")
