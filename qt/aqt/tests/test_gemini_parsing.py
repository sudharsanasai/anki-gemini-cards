#!/usr/bin/env python3
"""
Test script for the updated Gemini API parsing logic
"""

import sys
from pathlib import Path

# Add the qt/aqt directory to the path so we can import GeminiAPI
sys.path.insert(0, str(Path(__file__).parent / "qt" / "aqt"))

from gemini_api import GeminiAPI

def test_parse_cards():
    """Test the parse_cards method with various scenarios"""
    
    # Create a mock GeminiAPI instance (we won't actually call the API)
    api = GeminiAPI.__new__(GeminiAPI)
    
    # Test case 1: Simple Q&A
    print("=== Test 1: Simple Q&A ===")
    simple_text = """Q: What is the capital of France?
A: Paris is the capital of France."""
    
    cards = api.parse_cards(simple_text)
    print(f"Found {len(cards)} cards")
    for i, (front, back) in enumerate(cards, 1):
        print(f"Card {i}:")
        print(f"  Front: {front}")
        print(f"  Back: {back}")
        print()
    
    # Test case 2: Multi-line answer with HTML
    print("=== Test 2: Multi-line answer with HTML ===")
    html_text = """Q: What is the official name and type of government in Mexico, and what is its legislative structure?
A: Mexico's official name is the <b>United Mexican States</b> (<i>Estados Unidos Mexicanos</i>), and it operates as a <b>federal republic</b>.
<ul>
    <li><b>Head of State:</b> The President serves as both the head of state and head of government. As of the document's publication, the president is Andrés Manuel López Obrador, who began his single, non-renewable six-year term on December 1, 2018.</li>
    <li><b>Legislative Branch:</b> The legislature is a bicameral <b>National Congress</b> (<i>Congreso de la Unión</i>), which consists of two chambers:
        <ol>
            <li>The <b>Senate</b> (<i>Cámara de Senadores</i>)</li>
            <li>The <b>Chamber of Deputies</b> (<i>Cámara de Diputados</i>)</li>
        </ol>
    </li>
    <li><b>Key Historical Date:</b> Mexico declared its independence from Spain on September 16, 1810.</li>
</ul>"""
    
    cards = api.parse_cards(html_text)
    print(f"Found {len(cards)} cards")
    for i, (front, back) in enumerate(cards, 1):
        print(f"Card {i}:")
        print(f"  Front: {front}")
        print(f"  Back length: {len(back)} characters")
        print(f"  Back preview: {back[:100]}...")
        print(f"  Contains HTML tags: {'<b>' in back and '<ul>' in back}")
        print()
    
    # Test case 3: Multiple Q&A pairs
    print("=== Test 3: Multiple Q&A pairs ===")
    multiple_text = """Q: What is 2+2?
A: 2+2 equals 4.

Q: What is the largest planet in our solar system?
A: Jupiter is the largest planet in our solar system.
It has a mass more than twice that of Saturn.
Jupiter is known for its Great Red Spot."""
    
    cards = api.parse_cards(multiple_text)
    print(f"Found {len(cards)} cards")
    for i, (front, back) in enumerate(cards, 1):
        print(f"Card {i}:")
        print(f"  Front: {front}")
        print(f"  Back: {back}")
        print()
    
    # Test case 4: Edge case - answer with no content on A: line
    print("=== Test 4: Answer with no content on A: line ===")
    edge_text = """Q: What are the benefits of exercise?
A:
Exercise provides numerous health benefits including:
- Improved cardiovascular health
- Increased strength and flexibility
- Better mental health
- Weight management"""
    
    cards = api.parse_cards(edge_text)
    print(f"Found {len(cards)} cards")
    for i, (front, back) in enumerate(cards, 1):
        print(f"Card {i}:")
        print(f"  Front: {front}")
        print(f"  Back: {back}")
        print()

def test_real_world_scenario():
    """Test with a real-world scenario similar to what you encountered"""
    print("=== Real-world Scenario Test ===")
    
    api = GeminiAPI.__new__(GeminiAPI)
    
    # Simulate the actual response you showed
    real_response = """Q: What is the official name and type of government in Mexico, and what is its legislative structure?
A: Mexico's official name is the <b>United Mexican States</b> (<i>Estados Unidos Mexicanos</i>), and it operates as a <b>federal republic</b>.
<ul>
    <li><b>Head of State:</b> The President serves as both the head of state and head of government. As of the document's publication, the president is Andrés Manuel López Obrador, who began his single, non-renewable six-year term on December 1, 2018.</li>
    <li><b>Legislative Branch:</b> The legislature is a bicameral <b>National Congress</b> (<i>Congreso de la Unión</i>), which consists of two chambers:
        <ol>
            <li>The <b>Senate</b> (<i>Cámara de Senadores</i>)</li>
            <li>The <b>Chamber of Deputies</b> (<i>Cámara de Diputados</i>)</li>
        </ol>
    </li>
    <li><b>Key Historical Date:</b> Mexico declared its independence from Spain on September 16, 1810.</li>
</ul>
Adding card:
Front: What is the official name and type of government in Mexico, and what is its legislative structure?
Back: Mexico's official name is the <b>United Mexican States</b> (<i>Estados Unidos Mexicanos</i>), and it operates as a <b>federal republic</b>.
----------------------------------------"""
    
    cards = api.parse_cards(real_response)
    print(f"Found {len(cards)} cards")
    for i, (front, back) in enumerate(cards, 1):
        print(f"Card {i}:")
        print(f"  Front: {front}")
        print(f"  Back length: {len(back)} characters")
        print(f"  Contains complete answer: {'<ul>' in back and '<li>' in back and 'Senate' in back}")
        print(f"  Contains HTML formatting: {'<b>' in back and '<i>' in back}")
        print(f"  Back preview: {back[:200]}...")
        print()

if __name__ == "__main__":
    print("Testing Gemini API parsing logic...")
    print("=" * 50)
    
    test_parse_cards()
    test_real_world_scenario()
    
    print("All tests completed!") 