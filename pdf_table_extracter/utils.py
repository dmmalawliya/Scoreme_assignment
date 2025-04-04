import pandas as pd

def save_table_to_excel(table_data, output_path):
    df = pd.DataFrame(table_data)
    df.to_excel(output_path, index=False, header=False)
