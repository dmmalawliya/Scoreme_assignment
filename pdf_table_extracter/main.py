import os
import logging
import concurrent.futures
from tqdm import tqdm
from extractor import extract_words_from_pdf_plumber as extract_words_from_pdf, group_words_to_rows, extract_table_from_rows
from utils import save_table

# Configure logging
logging.basicConfig(filename="error.log", level=logging.ERROR, format="%(asctime)s - %(levelname)s - %(message)s")

# Directory paths
input_dir = "samples/input/"
output_dir = "samples/output/"
file_format = "xlsx"  # Change to "csv" if needed

# Ensure input and output directories exist
if not os.path.exists(input_dir):
    print(f"⚠️ Input directory '{input_dir}' not found. Creating it now...")
    os.makedirs(input_dir)

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def process_pdf(file):
    """Processes a single PDF and extracts tables."""
    pdf_path = os.path.join(input_dir, file)
    print(f"\n📄 Processing: {file}")

    try:
        pages = extract_words_from_pdf(pdf_path)

        if not pages:
            print(f"⚠️ No text extracted from {file}")
            logging.warning(f"No text found in {file}")
            return file  # Skip this file

        for page_num, words in enumerate(pages):
            grouped = group_words_to_rows(words)
            if not grouped:
                print(f"⚠️ No rows detected in {file}, page {page_num + 1}")
                logging.warning(f"No table structure detected in {file}, page {page_num + 1}")
                continue  # Skip empty pages

            table = extract_table_from_rows(grouped)
            output_file = os.path.join(output_dir, f"{file.replace('.pdf', '')}_page_{page_num + 1}.{file_format}")

            save_table(table, output_file, file_format)
            print(f"✅ Table saved: {output_file}")

    except Exception as e:
        print(f"❌ Error processing {file}: {e}")
        logging.error(f"Error processing {file}: {e}")

    return file  # Return file name when done

# List PDF files in input directory
input_files = [f for f in os.listdir(input_dir) if f.endswith(".pdf")]

if not input_files:
    print(f"⚠️ No PDF files found in {input_dir}. Please add files and try again.")
else:
    # Multi-threaded PDF processing
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = list(tqdm(executor.map(process_pdf, input_files), total=len(input_files), desc="Processing PDFs", unit="file"))

    print("\n✅ All PDFs processed successfully!")



