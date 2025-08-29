# Bajaj_API

A simple Flask REST API for processing arrays of strings—separating digits, letters, and special characters, performing numeric operations, and generating structured responses.

---

##  API Endpoint

### POST `/bfhl` or `/`

**Description:**  
Accepts a JSON payload with a `data` array of strings. Outputs a JSON response containing categorized data, numeric sum, and concatenated alphabetic string with case alternation.

**Request Body Example:**

```json
{
  "data": ["2", "a", "y", "4", "&", "-", "*", "5", "92", "b"]
}
