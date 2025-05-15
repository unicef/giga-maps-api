import requests
import json
import time
import csv
import nbformat
from nbformat.v4 import new_notebook, new_code_cell


# --------- Configuration ---------
BEARER_TOKEN = "place_your_API_KEY_here"  # Replace with your actual token
PAGE_SIZE = 1000
isocode3 = "BIH"  # Change this to fetch for a different country
USE_COUNTRY_ENDPOINT = True  # Set to False to use the general endpoint

# --------- URL Setup ---------
if USE_COUNTRY_ENDPOINT:
    BASE_URL = f"https://uni-ooi-giga-maps-service.azurewebsites.net/api/v1/schools_location/country/{isocode3}"
    prefix = f"schools_location_data_{isocode3}"
else:
    BASE_URL = "https://uni-ooi-giga-maps-service.azurewebsites.net/api/v1/schools_location"
    prefix = "schools_location_data_all"

# --------- Output Files ---------
CSV_OUTPUT_FILE = f"{prefix}.csv"
NOTEBOOK_OUTPUT_FILE = f"{prefix}.ipynb"

HEADERS = {
    "Authorization": f"Bearer {BEARER_TOKEN}",
    "Accept": "application/json"
}

# --------- Data Fetch Function ---------
def fetch_all_data():
    all_data = []
    page = 1

    while True:
        params = {
            "page": page,
            "size": PAGE_SIZE
        }

        try:
            response = requests.get(BASE_URL, headers=HEADERS, params=params)
            response.raise_for_status()
            parsed = response.json()
            data = parsed.get("data", [])
        except requests.exceptions.RequestException as e:
            print(f"Request failed on page {page}: {e}")
            break

        if not data:
            print(f"No data on page {page}. Stopping.")
            break

        all_data.extend(data)
        print(f"Fetched page {page} with {len(data)} records")

        if len(data) < PAGE_SIZE:
            break

        page += 1
        time.sleep(0.2)

    return all_data


# --------- Save to CSV ---------
def save_to_csv(data, filename):
    if not data:
        print("No data to save.")
        return

    keys = data[0].keys()

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)

    print(f"Saved {len(data)} records to {filename}")

# --------- Save to Jupyter Notebook ---------
def save_to_notebook(data, filename):
    nb = new_notebook()
    code = f"import json\n\ndata = {json.dumps(data, indent=2)}\n\nprint(f'Total records: {{len(data)}}')"
    nb.cells.append(new_code_cell(code))

    with open(filename, "w", encoding="utf-8") as f:
        nbformat.write(nb, f)

    print(f"Saved data to Jupyter notebook: {filename}")

# --------- Main ---------
if __name__ == "__main__":
    data = fetch_all_data()
    save_to_csv(data, CSV_OUTPUT_FILE)
    save_to_notebook(data, NOTEBOOK_OUTPUT_FILE)
