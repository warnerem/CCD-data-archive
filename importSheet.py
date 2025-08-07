import sqlite3
import csv
import requests
from io import StringIO
import re


SHEET_CSV_URL = "https://docs.google.com/spreadsheets/d/17e76UB-x4FCAfSqChfIF99eVLWw7hoNw0g1uoaENt0A/gviz/tq?tqx=out:csv"

def clean_header_for_sql(header_text):
    """Cleans a string to be a valid and readable SQL column name."""
    if not header_text:

        return "unnamed_column"

    clean = header_text.lower()

    clean = re.sub(r'[^a-z0-9_]+', '_', clean)

    clean = clean.strip('_')
    return clean

response = requests.get(SHEET_CSV_URL)
response.raise_for_status()
csv_text = response.text
print("Data fetched")


reader = csv.reader(StringIO(csv_text))
all_rows = list(reader)

if len(all_rows) < 1:
    print("CSV file is empty")
    exit()

header_row = all_rows[0]
data_rows = all_rows[1:]


col_names = [clean_header_for_sql(h) for h in header_row]
num_cols = len(col_names)
print(f"Detected {num_cols} columns: {col_names}")


TABLE_NAME = 'data_archive'
DB_NAME = 'data.db'
conn = sqlite3.connect(DB_NAME)
c = conn.cursor()

cols_with_types = ', '.join([f'"{col}" TEXT' for col in col_names])
c.execute(f"DROP TABLE IF EXISTS {TABLE_NAME}")
c.execute(f"CREATE TABLE {TABLE_NAME} ({cols_with_types})")

placeholders = ', '.join(['?'] * num_cols)
rows_inserted = 0
for row in data_rows:

    while len(row) < num_cols:
        row.append('')

    row = row[:num_cols]
    
    c.execute(f"INSERT INTO {TABLE_NAME} VALUES ({placeholders})", row)
    rows_inserted += 1


conn.commit()
conn.close()

