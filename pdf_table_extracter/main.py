from extractor import extract_words_from_pdf, group_words_to_rows, extract_table_from_rows
from utils import save_table_to_excel
import os

input_dir = "samples/input/"
output_dir = "samples/output/"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for file in os.listdir(input_dir):
    if file.endswith(".pdf"):
        print(f"Processing {file}...")
        pdf_path = os.path.join(input_dir, file)
        pages = extract_words_from_pdf(pdf_path)

        for page_num, words in enumerate(pages):
            grouped = group_words_to_rows(words)
            table = extract_table_from_rows(grouped)

            output_file = os.path.join(
                output_dir,
                file.replace(".pdf", f"_page_{page_num + 1}.xlsx")
            )
            save_table_to_excel(table, output_file)
        print(f"Finished: {file}\n")
