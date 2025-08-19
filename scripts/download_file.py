import requests
from requests.exceptions import RequestException

def extract_icco_data(**kwargs):
    """
    Airflow Task: Extracts the raw CSV data from the ICCO website.
    Pushes the CSV text to XCom for downstream tasks.
    
    Returns:
        str: The raw CSV data as a string.
    """
    csv_url = "https://www.icco.org/wp-content/uploads/Price-Stats.csv"
    headers = {'User-Agent': 'ICCO-Data-Pipeline/1.0 (etl-bot@example.com)'}
    
    try:
        response = requests.get(csv_url, headers=headers)
        response.raise_for_status() # Raises exception for 4XX/5XX errors
        
        csv_data = response.text
        # Push to XCom so the transform task can use it
        kwargs['ti'].xcom_push(key='raw_csv_data', value=csv_data)
        
        return csv_data
        
    except RequestException as e:
        raise RuntimeError(f"Failed to extract data from {csv_url}: {str(e)}")

extract_icco_data()
