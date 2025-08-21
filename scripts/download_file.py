import requests
import logging as logger
from requests.exceptions import RequestException
from bs4 import BeautifulSoup

def extract_icco_data(**kwargs):
    """
    Airflow Task: Extracts the raw CSV data from the ICCO website.
    First finds the correct CSV URL from the statistics page, then downloads the data.
    Pushes the CSV text to XCom for downstream tasks.

    """
    # URL of the main statistics page
    stats_page_url = "https://www.icco.org/statistics"
    headers = {'User-Agent': 'ICCO-Data-Pipeline/1.0 (etl-bot@example.com)'}
    
    try:
        # 1. First, get the main statistics page
        logger.info(f"Fetching statistics page: {stats_page_url}")
        page_response = requests.get(stats_page_url, headers=headers)
        page_response.raise_for_status()
        
        # 2. Parse the HTML to find the CSV download link
        soup = BeautifulSoup(page_response.content, 'html.parser')
        
        # Look for the download button/link. This selector might need adjustment.
        # Inspect the page to find the correct element.
        csv_link_element = soup.find('a', href=True, string='Download CSV')
        if not csv_link_element:
            # Try alternative selectors if the first one doesn't work
            csv_link_element = soup.find('a', {'href': lambda x: x and '.csv' in x})
        
        if not csv_link_element:
            raise RuntimeError("Could not find CSV download link on the statistics page")
        
        # Get the href attribute and make sure it's a full URL
        csv_relative_path = csv_link_element['href']
        if csv_relative_path.startswith('/'):
            # If it's a relative path, build the full URL
            csv_url = f"https://www.icco.org{csv_relative_path}"
        else:
            csv_url = csv_relative_path
        
        logger.info(f"Found CSV URL: {csv_url}")
        
        # 3. Now download the actual CSV data
        logger.info(f"Downloading CSV data from: {csv_url}")
        csv_response = requests.get(csv_url, headers=headers)
        csv_response.raise_for_status()
        
        csv_data = csv_response.text
        
        # Push to XCom so the transform task can use it
        if 'ti' in kwargs:
            kwargs['ti'].xcom_push(key='raw_csv_data', value=csv_data)
        
        return csv_data
        
    except RequestException as e:
        error_msg = f"Failed to extract data: {str(e)}"
        logger.error(error_msg)
        raise RuntimeError(error_msg)

#checking
extract_icco_data()
