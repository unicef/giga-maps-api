# FAQs

## Frequently Asked Questions

### 1. How do I get an API key?
You can request an API key by visiting the [Giga Maps API Dashboard](https://maps.giga.global/docs/explore-api).  
- Log in and select the API you are interested in.  
- Open the documentation and click **Request**.  
- Once approved, your API key will appear under **API Keys** in the left panel.  

---

### 2. Do I need a different API key for each endpoint?
Yes. Each API has its own API key. You must request a key for every API you plan to use.  
- **Public APIs**: Keys are approved automatically.  
- **Private APIs**: You will be asked to provide more details. The Giga team reviews requests manually (1–2 business days).  

---

### 3. Where can I see my API keys?
Log in to the [Giga Maps API Dashboard](https://maps.giga.global/docs/explore-api).  
Navigate to **API Keys** in the left menu. You can copy the keys from there.  

---

### 4. Why is my API key not working?
- Check that the key you are using belongs to the correct API. Keys are not interchangeable.  
- Make sure you include it in your request header as follows:  
  ```
  Authorization: Bearer <your-api-key>
  ```
- If your key is for a private API, ensure it has been approved by the Giga team.  

---

### 5. How do I test the APIs with my key?
Use the **Try it out** feature in the documentation UI. Paste your API key into the authorization field and submit. You can also test using curl, for example:
```bash
curl -X GET "https://uni-ooi-giga-maps-service.azurewebsites.net/api/v1/countries" \
  -H "Authorization: Bearer <your-api-key>"
```

---

### 6. Do I need to include an Accept header?
Yes, it’s recommended to include:  
```
Accept: application/json
```
This ensures you always receive JSON-formatted responses.

---

### 7. What should I do if my request returns 404 Not Found?
- Verify the endpoint path matches the documentation exactly.  
- Ensure you are using the correct base URL (`/api/v1`).  
- Double-check query parameters like `country_iso3_code` are spelled correctly.  

---

### 8. How can I change between the Production server, Giga Meter server and Mock server?
In the documentation UI, you can select the **server** dropdown at the top.  
- **Production server**: Returns live Giga maps data.
- **Giga Meter server**: Returns live Giga Meter data and measurements.  
- **Mock server**: Returns example responses for testing without consuming real data.  

---

### 9. How do I access Giga Meter data?
Use the Giga Meter endpoints (`/dailycheckapp_countries`, `/dailycheckapp_schools`, `/measurements`).  
These require a separate API key from the Giga Meter backend server:  
```
https://uni-ooi-giga-meter-backend.azurewebsites.net/api/v1
```

---

### 10. Who do I contact if I still can’t access the data?
Email the Giga team at [gigabcn@unicef.org](mailto:gigabcn@unicef.org) for further assistance.  
You will also receive automated emails from **gigamaps.noreply@mail.unicef.org** when your API key requests are approved.
