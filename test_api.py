import requests
import json

# Local URL (Flask defaults to 5000, but we set it to 8000 in main.py)
URL = "http://127.0.0.1:8000/predict"

# Mock data mimicking a high-risk scenario to test the mapping
payload = {
    "age": 22,
    "gender": "Female",
    "marital_status": "Single",
    "education": "Undergraduate", # Use 'education' not 'education_level'
    "employment": "Unemployed",
    "sleep_hou": 4.0,
    "physical_a": 1.0,
    "screen_tin": 10.0,
    "social_sup": 2,
    "work_stres": 9,
    "academic_": 8,
    "job_satisfa": 2,
    "financial_s": 2,
    "working_h": 60,
    "anxiety_so": 9,
    "depression": 8,
    "stress_leve": 9,
    "mood_swi": 2,
    "concentra": 8,
    "panic_atta": 1,
    "family_hist": 1,
    "previous_r": 1,
    "therapy_hi": 1,
    "substance": 0
}

def test_model():
    print(f"📡 Connecting to API at {URL}...")
    try:
        response = requests.post(URL, json=payload)
        if response.status_code == 200:
            res = response.json()
            p = res['prediction']
            print("\n✅ API TEST SUCCESSFUL")
            print(f"Result: {p['risk_level']} (Score: {p['score']})")
            print(f"Advice: {p['recommendation']}")
        else:
            print(f"❌ Error: {response.status_code}")
            print(response.text)
    except Exception as e:
        print(f"🚨 Connection failed. Is the API running? Error: {e}")

if __name__ == "__main__":
    test_model()