import requests

url = "http://0.0.0.0:9696/predict"

lead = {
  "lead_source": "organic_search",
  "industry": "technology",
  "employment_status": "employed",
  "location": "europe",
  "number_of_courses_viewed": 4,
  "annual_income": 80304.0,
  "interaction_count": 7,
  "lead_score": 0.74
}

response = requests.post(url, json=lead).json()
print(response)
print(round(response['conversion_probability'], 3))