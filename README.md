# PDF Table Extraction Tool - Documentation

## Overview
This tool extracts tables from system-generated PDFs, including those with or without borders and irregular shapes. The extracted data is stored in Excel (`.xlsx`) or CSV (`.csv`) format.

---

## Installation and Setup

### 1️⃣ Prerequisites
Ensure you have **Python 3.8+** installed on your system.

### 2️⃣ Install Dependencies
Run the following command to install required libraries:
```sh
pip install -r requirements.txt
```
If `requirements.txt` is missing, install dependencies manually:
```sh
pip install pdfplumber PyPDF2 pandas openpyxl tqdm
```

### 3️⃣ Folder Structure
Ensure the following directory structure exists:
```
project_folder/
│── main.py          # Main script to run
│── extractor.py     # Extracts tables from PDFs
│── utils.py         # Helper functions for saving tables
│── requirements.txt # List of required Python packages
│── samples/
│   ├── input/       # Store PDFs to be processed
│   ├── output/      # Extracted tables are saved here
```

---

## How to Run the Tool

1️⃣ **Place PDFs in `samples/input/` directory.**
2️⃣ **Run the script:**
```sh
python main.py
```
3️⃣ **Extracted tables will be saved in `samples/output/` as .xlsx or .csv files.**

---

## Configuration
Modify the following parameters in `main.py` as needed:
```python
input_dir = "samples/input/"   # Input directory for PDFs
output_dir = "samples/output/" # Output directory for tables
file_format = "xlsx"  # Change to "csv" if needed
```

---

## Error Handling
- Errors are logged in `error.log`.
- If no tables are detected, a warning is logged but processing continues.

---

## Advanced Features
✅ GUI for drag-and-drop PDFs
✅ Multi-threading for faster processing
✅ Flask/Django-based web app
✅ CSV export
✅ Enhanced error handling

---

## Troubleshooting
**Issue:** `ModuleNotFoundError: No module named 'pdfplumber'`
**Solution:** Install missing dependencies using:
```sh
pip install pdfplumber
```

**Issue:** `No tables detected in the PDF`
**Solution:** Try using another extraction method (`PyPDF2` instead of `pdfplumber`).

---

## Contact
For issues or feature requests, contact: [dmmalawliya@gmail.com]

