"""
Monster Generator for WFRP 1st Edition
Expand monsters and abilities by editing data/monsters.json.
"""
import random
import json
import os

data_dir = os.path.join(os.path.dirname(__file__), 'data')

def load_json(filename):
    with open(os.path.join(data_dir, filename), 'r', encoding='utf-8') as f:
        return json.load(f)

def generate_monster():
    monsters = load_json('monsters.json')
    monster = random.choice(monsters)
    return monster

if __name__ == "__main__":
    print(generate_monster())
