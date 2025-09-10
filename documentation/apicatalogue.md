# API Overview



| Category                   | Access Level | Endpoint                                      | Description                                                              |
|----------------------------|--------------|-----------------------------------------------|---------------------------------------------------------------------------|
| Country List               | Public       | `/api/v1/countries` (license: ODbL v1.0)       | Lists all countries with data on Giga Maps                               |
| School Geolocation Data    | Public       | `/api/v1/schools_location` (license: ODbL v1.0)| Returns coordinates (lat, lon) and school IDs and names per country     |
| Giga Meter - Countries     | Private      | `/api/v1/dailycheckapp_countries`             | Lists all countries where Giga Meter is installed                        |
| Giga Meter - Schools       | Private      | `/api/v1/dailycheckapp_schools`               | Lists all schools where Giga Meter is installed                          |
| Giga Meter - Measurements  | Private      | `/api/v1/measurements`                        | Returns latency, upload, and download speed from Giga Meter             |
| School Profile             | Private      | `/api/v1/schools_profile`                     | Provides connectivity status and school-related metadata                |
| Real-time Internet Quality | Private      | `/api/v1/all_measurements`                    | Returns monitoring data including Giga Meter and other sources          |
