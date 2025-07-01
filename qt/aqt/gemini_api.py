import json
import requests
import os

class GeminiAPI:
    def __init__(self, api_key=None, instruction_path="/Users/sudharsanasaithambi/Desktop/Code/drona/anki/qt/aqt/llm_instruction.json", config_path="/Users/sudharsanasaithambi/Desktop/Code/drona/anki/qt/aqt/gemini_config.json"):
        self.instruction_path = instruction_path
        self.api_url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-pro:generateContent"
        if api_key is not None:
            self.api_key = api_key
        else:
            # Try to read from config file
            try:
                with open(config_path, "r") as f:
                    config = json.load(f)
                self.api_key = config["api_key"]
            except Exception as e:
                raise RuntimeError(f"Gemini API key not found. Please set it in {config_path}.") from e

    def load_instruction(self):
        with open(self.instruction_path, "r") as f:
            data = json.load(f)
        return data["instruction"]

    def generate_cards(self, topic, num_cards):
        instruction = self.load_instruction().format(topic=topic, num_cards=num_cards)
        payload = {
            "contents": [{"parts": [{"text": instruction}]}]
        }
        headers = {"Content-Type": "application/json"}
        params = {"key": self.api_key}
        response = requests.post(self.api_url, headers=headers, params=params, json=payload)
        print("Raw Gemini API response:", response.text)  # Debug print
        response.raise_for_status()
        data = response.json()
        # Parse the response to extract Q&A pairs
        text = data["candidates"][0]["content"]["parts"][0]["text"]
        print("LLM raw response:\n", text)  # Debug print
        cards = self.parse_cards(text)
        return cards

    def parse_cards(self, text):
        # Accepts 'Question:', 'Q:', 'Answer:', 'A:'
        cards = []
        lines = text.splitlines()
        front, back = None, None
        current_answer_lines = []
        in_answer = False
        
        for line in lines:
            l = line.strip().lower()
            if l.startswith("question:") or l.startswith("q:"):
                # If we have a previous Q&A pair, save it
                if front is not None and current_answer_lines:
                    back = "\n".join(current_answer_lines).strip()
                    cards.append((front, back))
                
                # Start new question
                front = line.split(":", 1)[1].strip()
                current_answer_lines = []
                in_answer = False
                
            elif l.startswith("answer:") or l.startswith("a:"):
                # Start collecting answer lines
                in_answer = True
                answer_content = line.split(":", 1)[1].strip()
                if answer_content:  # Only add if there's content on the same line
                    current_answer_lines.append(answer_content)
                    
            elif front is not None and in_answer:
                # Continue collecting answer lines (for multi-line answers)
                current_answer_lines.append(line)
        
        # Don't forget the last Q&A pair
        if front is not None and current_answer_lines:
            back = "\n".join(current_answer_lines).strip()
            cards.append((front, back))
            
        return cards 