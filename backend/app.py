"""
Main API entry point for WFRP Helper Tool
Run with: python app.py
"""
from flask import Flask, jsonify, request
from character_generator import generate_character
from monster_generator import generate_monster
from quest_generator import generate_quest
from dice_roller import roll_dice
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/character', methods=['GET'])
def api_character():
    return jsonify(generate_character())

@app.route('/api/monster', methods=['GET'])
def api_monster():
    return jsonify(generate_monster())

@app.route('/api/quest', methods=['GET'])
def api_quest():
    return jsonify(generate_quest())

@app.route('/api/dice', methods=['GET'])
def api_dice():
    sides = int(request.args.get('sides', 6))
    count = int(request.args.get('count', 1))
    result = roll_dice(sides, count)
    return jsonify({'result': result})

if __name__ == "__main__":
    app.run(debug=True)
