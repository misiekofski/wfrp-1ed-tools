"""
Dice Roller for WFRP 1st Edition
Roll any dice (d6, d20, d100, etc.)
"""
import random

def roll_dice(sides, count=1):
    return [random.randint(1, sides) for _ in range(count)]

if __name__ == "__main__":
    print('d6:', roll_dice(6))
    print('d20:', roll_dice(20))
    print('d100:', roll_dice(100))
