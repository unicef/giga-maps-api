# Resources

## Download through scripts and Jupyter notebooks

Access the data programmatically using the APIs.

You can authorize with your credentials and test the endpoints directly on this page.

To download full datasets beyond the API’s pagination limits, you can use a script to loop through all pages.

## School Location API

- For a sample Python script to download school location data, click here: [Link](https://github.com/unicef/giga-maps-api)
- For a sample Jupyter Notebook to download school location data, click here: [Link](https://github.com/unicef/giga-maps-api/tree/main?tab=readme-ov-file#using-jupyter-notebook)

Through GigaSpatial you can use the code below to download the school location data:

```python
# Get school data
gslf = GigaSchoolLocationFetcher(country = country_code)
df_schools = gslf.fetch_locations()
```

Check out the [GigaSpatial repository](https://github.com/unicef/giga-spatial) to learn more.

## School Profile API

- For a sample Jupyter Notebook to download school profile data, click here: [Link](https://github.com/unicef/giga-maps-api/blob/main/Access_school_profile_API.ipynb)
