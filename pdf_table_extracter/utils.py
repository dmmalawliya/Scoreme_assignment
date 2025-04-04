import pandas as pd
from openpyxl import load_workbook

def save_table_to_excel(table_data, output_path):
    df = pd.DataFrame(table_data)
    
    with pd.ExcelWriter(output_path, engine="openpyxl") as writer:
        df.to_excel(writer, index=False, header=False)

        # Auto-adjust column widths
        workbook = writer.book
        worksheet = writer.sheets["Sheet1"]
        for col in worksheet.columns:
            max_length = 0
            col_letter = col[0].column_letter  # Get column letter
            for cell in col:
                try:
                    max_length = max(max_length, len(str(cell.value)))
                except:
                    pass
            worksheet.column_dimensions[col_letter].width = max_length + 2


def save_table_to_csv(table_data, output_path):
    df = pd.DataFrame(table_data)
    df.to_csv(output_path, index=False, header=False)

def save_table(table_data, output_path, file_format="xlsx"):
    """Saves table data as either Excel or CSV based on user preference."""
    if file_format == "xlsx":
        save_table_to_excel(table_data, output_path)
    elif file_format == "csv":
        save_table_to_csv(table_data, output_path)
    else:
        raise ValueError("Unsupported file format. Choose 'xlsx' or 'csv'.")