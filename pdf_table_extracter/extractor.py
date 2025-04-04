import logging
import pdfplumber
import PyPDF2  # Make sure PyPDF2 is installed

logging.basicConfig(filename="error.log", level=logging.ERROR)

def extract_words_from_pdf_plumber(pdf_path):
    """Extracts structured words from a PDF using pdfplumber."""
    all_pages = []
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                words = page.extract_words(extra_attrs=["x0", "x1", "top", "bottom"])
                if not words:
                    logging.warning(f"No words detected in {pdf_path}, page {page.page_number}")
                all_pages.append(words)
    except Exception as e:
        logging.error(f"Error processing {pdf_path}: {str(e)}")
    return all_pages

def extract_words_from_pdf_pypdf(pdf_path):
    """Extracts raw text from a PDF using PyPDF2 (alternative method)."""
    extracted_text = []
    try:
        with open(pdf_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                extracted_text.append(page.extract_text() or "")
    except Exception as e:
        logging.error(f"Error processing {pdf_path}: {e}")
    return extracted_text

def group_words_to_rows(words, tolerance=3):
    """Groups words into rows based on vertical proximity."""
    rows = {}
    for word in words:
        top = round(word["top"] / tolerance) * tolerance
        rows.setdefault(top, []).append(word)

    sorted_rows = [sorted(row, key=lambda w: w["x0"]) for row in rows.values()]
    sorted_rows = sorted(sorted_rows, key=lambda r: r[0]["top"])

    # Merge multi-line cells by checking words that are close in X position
    for row in sorted_rows:
        for i in range(len(row) - 1):
            if abs(row[i]["x1"] - row[i + 1]["x0"]) < 5:  # Small gap, merge text
                row[i + 1]["text"] = row[i]["text"] + " " + row[i + 1]["text"]
                row[i]["text"] = ""  # Mark old text as merged

    # Remove empty merged cells
    cleaned_rows = [[word for word in row if word["text"]] for row in sorted_rows]

    return cleaned_rows

def extract_table_from_rows(grouped_rows):
    """Converts grouped words into a structured table format."""
    table = []
    max_cols = max(len(row) for row in grouped_rows)

    for row in grouped_rows:
        table_row = [word["text"] for word in row]

        # Fill missing cells with empty values for consistency
        while len(table_row) < max_cols:
            table_row.append("")

        table.append(table_row)
    
    return table


