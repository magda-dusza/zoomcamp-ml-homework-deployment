import pickle

input_path = "pipeline.bin"
with open(input_path, 'rb') as f_in:
    dv, model = pickle.load(f_in)

lead = {
  "lead_source": "paid_ads",
  "industry": "technology",
  "employment_status": "employed",
  "location": "north_america",
  "number_of_courses_viewed": 2,
  "annual_income": 79276.0,
  "interaction_count": 4,
  "lead_score": 0.41
}

X = dv.transform(lead)
y_pred = model.predict_proba(X)[:, 1]

print(y_pred.round(3))