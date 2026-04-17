# import requests
# import json

# # Local URL (Flask defaults to 5000, but we set it to 8000 in main.py)
# URL = "http://127.0.0.1:8000/predict"

# # Mock data mimicking a high-risk scenario to test the mapping
# payload = {
#     "age": 50,
#     "gender": "Female",
#     "marital_status": "Single",
#     "education": "Undergraduate", # Use 'education' not 'education_level'
#     "employment": "Unemployed",
#     "sleep_hou": 4.0,
#     "physical_a": 3.0,
#     "screen_tin": 20.0,
#     "social_sup": 5,
#     "work_stres": 9,
#     "academic_": 8,
#     "job_satisfa": 2,
#     "financial_s": 2,
#     "working_h": 60,
#     "anxiety_so": 9,
#     "depression": 8,
#     "stress_leve": 9,
#     "mood_swi": 2,
#     "concentra": 8,
#     "panic_atta": 1,
#     "family_hist": 1,
#     "previous_r": 1,
#     "therapy_hi": 1,
#     "substance": 0
# }

# def test_model():
#     print(f"📡 Connecting to API at {URL}...")
#     try:
#         response = requests.post(URL, json=payload)
#         if response.status_code == 200:
#             res = response.json()
#             p = res['prediction']
#             print("\n✅ API TEST SUCCESSFUL")
#             print(f"Result: {p['risk_level']} (Score: {p['score']})")
#             print(f"Advice: {p['recommendation']}")
#         else:
#             print(f"❌ Error: {response.status_code}")
#             print(response.text)
#     except Exception as e:
#         print(f"🚨 Connection failed. Is the API running? Error: {e}")

# if __name__ == "__main__":
#     test_model()

import requests

URL = "http://127.0.0.1:8000/predict"


# =========================
# EXACT MODEL FEATURE SET
# =========================
payload = {
    "age": 56,
    "gender": "Male",
    "marital_status": "Single",
    "education_level": "Bachelor",
    "employment_status": "Unemployed",

    "sleep_hours": 6.5,
    "physical_activity_hours_per_week": 3.0,
    "screen_time_hours_per_day": 8.0,

    "social_support_score": 7,
    "work_stress_level": 8,
    "academic_pressure_level": 5,
    "job_satisfaction_score": 6,
    "financial_stress_level": 7,
    "working_hours_per_week": 40,

    "stress_level": 7,
    "mood_swings_frequency": 5,
    "concentration_difficulty_level": 4,

    "panic_attack_history": 1,
    "family_history_mental_illness": 0,
    "previous_mental_health_diagnosis": 1,
    "therapy_history": 1,
    "substance_use": 0
}


# =========================
# TEST FUNCTION
# =========================
def test_api():
    print(f"📡 Sending request to {URL}\n")

    try:
        response = requests.post(URL, json=payload)

        if response.status_code == 200:
            res = response.json()["prediction"]

            print("✅ SUCCESS")
            print("----------------------")
            print(f"Risk Level: {res['risk_level']}")
            print(f"Risk Score: {res['risk_score']}")
            print(f"Color: {res['color']}")
            print(f"Advice: {res['recommendation']}")
            print("----------------------")

        else:
            print("❌ ERROR")
            print(response.json())

    except Exception as e:
        print(f"🚨 Connection error: {e}")


if __name__ == "__main__":
    test_api()