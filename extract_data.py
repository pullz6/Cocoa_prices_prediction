import pandas as pd
import os
from datetime import datetime

# Configuration
DOWNLOAD_FOLDER = "/Users/pulsaragunawardhana/Desktop/Projects/MLOps/ETL_Ecommerce"  # Where ICCO CSVs get saved
OUTPUT_FILE = "cocoa_stats_processed.csv"
LAST_DATE_FILE = "last_date.txt"

def get_latest_csv():
    """Find most recently downloaded ICCO CSV"""
    csv_files = [f for f in os.listdir(DOWNLOAD_FOLDER) 
                if f.lower().endswith('.csv') and 'cocoa' in f.lower()]
    if not csv_files:
        return None
    latest = max(csv_files, key=lambda f: os.path.getmtime(os.path.join(DOWNLOAD_FOLDER, f)))
    return os.path.join(DOWNLOAD_FOLDER, latest)

def extract_new_data(csv_path):
    """Extract only new records since last run"""
    # Read existing data if any
    existing_dates = set()
    if os.path.exists(OUTPUT_FILE):
        existing_df = pd.read_csv(OUTPUT_FILE)
        existing_dates = set(pd.to_datetime(existing_df['Date']).dt.strftime('%Y-%m-%d'))
    
    # Read new CSV (handling ICCO's multi-header format)
    with open(csv_path, 'r') as f:
        lines = [line for line in f if line.strip() and not line.startswith(('Date', 'date', 'YEAR'))]
    
    new_df = pd.read_csv(pd.compat.StringIO(''.join(lines)))
    
    # Standardize date column
    new_df['Date'] = pd.to_datetime(new_df['Date'], dayfirst=True, errors='coerce')
    new_df = new_df.dropna(subset=['Date'])
    new_df['Date_str'] = new_df['Date'].dt.strftime('%Y-%m-%d')
    
    # Filter for new records
    new_records = new_df[~new_df['Date_str'].isin(existing_dates)]
    
    if not new_records.empty:
        # Append to existing data
        if os.path.exists(OUTPUT_FILE):
            combined = pd.concat([existing_df, new_records.drop(columns=['Date_str'])])
        else:
            combined = new_records.drop(columns=['Date_str'])
        
        combined.to_csv(OUTPUT_FILE, index=False)
        print(f"Added {len(new_records)} new records")
    else:
        print("No new data found")

if __name__ == "__main__":
    latest_csv = get_latest_csv()
    if latest_csv:
        extract_new_data(latest_csv)
    else:
        print("No ICCO CSV files found in download folder")