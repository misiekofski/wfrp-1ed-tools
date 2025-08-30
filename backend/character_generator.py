"""
Character Generator for WFRP 1st Edition
Expand races, professions, and names by editing data/*.json files.
"""
import random
import json
import os

data_dir = os.path.join(os.path.dirname(__file__), 'data')

def load_json(filename):
    with open(os.path.join(data_dir, filename), 'r', encoding='utf-8') as f:
        return json.load(f)

def generate_character():
    races = load_json('races.json')
    professions = load_json('professions.json')
    names = load_json('names.json')
    stats = {
        'WS': random.randint(10, 50),
        'BS': random.randint(10, 50),
        'S': random.randint(10, 50),
        'T': random.randint(10, 50),
        'W': random.randint(1, 5),
        'I': random.randint(10, 50),
        'A': random.randint(1, 3),
        'Dex': random.randint(10, 50),
        'Ld': random.randint(10, 50),
        'Int': random.randint(10, 50),
        'Cl': random.randint(10, 50),
        'WP': random.randint(10, 50),
        'Fel': random.randint(10, 50)
    }
    race = random.choice(races)
    profession = random.choice(professions)
    name = random.choice(names[race])
    return {
        'name': name,
        'race': race,
        'profession': profession,
        'stats': stats
    }

if __name__ == "__main__":
    print(generate_character())
