import pdfplumber

def extract_words_from_pdf(pdf_path):
    all_pages = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            words = page.extract_words(extra_attrs=["x0", "x1", "top", "bottom"])
            all_pages.append(words)
    return all_pages

def group_words_to_rows(words, tolerance=3):
    rows = {}
    for word in words:
        top = round(word['top'] / tolerance) * tolerance
        rows.setdefault(top, []).append(word)
    sorted_rows = [sorted(row, key=lambda w: w['x0']) for row in rows.values()]
    return sorted(sorted_rows, key=lambda r: r[0]['top'])

def extract_table_from_rows(grouped_rows):
    table = []
    for row in grouped_rows:
        table_row = [word['text'] for word in row]
        table.append(table_row)
    return table
