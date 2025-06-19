
# Giga Schools Location Data Downloader

## Using the Python Script for API Access

This script allows you to download school location data from the Giga Maps API:

* All schools: `/api/v1/schools_location`
* Country-specific: `/api/v1/schools_location/country/{isocode3}`

You can export the data as:

* CSV
* Jupyter Notebook


### Requirements

Ensure you have Python 3 installed.

Install dependencies:

```bash
cd your-folder
python3 -m venv venv
source venv/bin/activate
pip install requests nbformat
```
* If needed: [How to install Python](https://realpython.com/installing-python/)



### How to Use

1. **Set your API token**

   Open the script and replace:

   ```python
   BEARER_TOKEN = "place_your_API_KEY_here"
   ```


with your actual token.

2. **Set the country code**

   Edit the `isocode3` variable:

   ```python
   isocode3 = "BIH"  # Example for Bosnia and Herzegovina
   ```
Get ISO3 codes: [https://www.iban.com/country-codes](https://www.iban.com/country-codes)


3. **Run the script**

   Execute the script:

   ```bash
   python schooldatalocation.py
   ```
---

## Using Jupyter Notebook

The notebook file `get_giga_maps_data_from_API.ipynb`in the repository allows you to fetch school geolocation data from the Giga Maps API interactively by selecting a country and entering your API key.


### 1. Load the notebook

#### Run locally in Jupyter

* Make sure you have Jupyter installed:

  ```bash
  pip install notebook
  ```
* Start Jupyter:

  ```bash
  jupyter notebook
  ```
* Navigate to the file `get_giga_maps_data_from_API.ipynb` and open it.



### 2. Set up your environment

Make sure the required Python packages are installed:

```bash
pip install requests pycountry ipywidgets pandas geopandas
```

If running in Colab, install geopandas with:

```python
!pip install geopandas
```


### 3. How to use it

Once the notebook is open:

1. **Select your country** using the dropdown. This automatically loads the ISO3 code.
2. **Paste your API key** into the `api_key` field (see Giga API access steps).
3. **Run all cells** (click "Runtime" > "Run all" in Colab, or press `Shift+Enter` step by step).
4. The notebook will:

   * Fetch the data in pages
   * Combine the results
   * Convert them into a spatial GeoDataFrame
   * Display a summary


### 4. Accessing the data

After running, the notebook saves the data to:

* `school_data.geojson`
  This file includes all school location points for the selected country in standard geospatial format.

You can:

* Load the GeoJSON in QGIS, Mapbox, or Python
* Visualize, filter, or export it using `geopandas` and `pandas`

---
