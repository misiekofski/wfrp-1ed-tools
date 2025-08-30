"""
Quest Generator for WFRP 1st Edition
Expand quests and complications by editing data/quests.json and data/complications.json.
"""
import random
import json
import os

data_dir = os.path.join(os.path.dirname(__file__), 'data')

def load_json(filename):
    with open(os.path.join(data_dir, filename), 'r', encoding='utf-8') as f:
        return json.load(f)

def generate_quest():
    quests = load_json('quests.json')
    complications = load_json('complications.json')
    quest = random.choice(quests)
    complication = random.choice(complications)
    return {
        'quest': quest,
        'complication': complication
    }

if __name__ == "__main__":
    print(generate_quest())
