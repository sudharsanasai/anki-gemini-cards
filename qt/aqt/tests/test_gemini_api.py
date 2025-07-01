import sys
import json
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from gemini_api import GeminiAPI

def main():
    if len(sys.argv) < 3:
        print("Usage: python test_gemini_api.py <topic> <num_cards>")
        sys.exit(1)
    topic = sys.argv[1]
    num_cards = int(sys.argv[2])
    gemini = GeminiAPI()
    instruction = gemini.load_instruction().format(topic=topic, num_cards=num_cards)
    payload = {
        "contents": [{"parts": [{"text": instruction}]}]
    }
    headers = {"Content-Type": "application/json"}
    params = {"key": gemini.api_key}
    import requests
    response = requests.post(gemini.api_url, headers=headers, params=params, json=payload)
    print("Raw Gemini API response:")
    print(response.text)
    try:
        data = response.json()
        print("\nParsed JSON:")
        print(json.dumps(data, indent=2))
    except Exception as e:
        print(f"\nError parsing JSON: {e}")

if __name__ == "__main__":
    main() 