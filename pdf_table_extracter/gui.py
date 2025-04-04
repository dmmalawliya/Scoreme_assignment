import os
import tkinter as tk
from tkinter import filedialog, messagebox
from extractor import extract_words_from_pdf, group_words_to_rows, extract_table_from_rows
from utils import save_table_to_excel, save_table_to_csv

def process_pdf(pdf_path, output_format):
    pages = extract_words_from_pdf(pdf_path)
    all_tables = []

    for page_num, words in enumerate(pages):
        grouped = group_words_to_rows(words)
        table = extract_table_from_rows(grouped)
        all_tables.append(table)

        output_file = pdf_path.replace(".pdf", f"_page_{page_num + 1}.{output_format}")
        if output_format == "xlsx":
            save_table_to_excel(table, output_file)
        else:
            save_table_to_csv(table, output_file)

    messagebox.showinfo("Success", f"Tables extracted and saved as {output_format.upper()}!")

def select_pdf():
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if file_path:
        format_choice = output_format.get()
        process_pdf(file_path, format_choice)

# GUI Setup
root = tk.Tk()
root.title("PDF Table Extractor")

tk.Label(root, text="Select a PDF and Extract Tables").pack(pady=10)
output_format = tk.StringVar(value="xlsx")
tk.Radiobutton(root, text="Save as Excel", variable=output_format, value="xlsx").pack()
tk.Radiobutton(root, text="Save as CSV", variable=output_format, value="csv").pack()
tk.Button(root, text="Select PDF & Extract", command=select_pdf).pack(pady=20)

root.mainloop()
