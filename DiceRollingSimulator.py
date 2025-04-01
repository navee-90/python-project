import random

def roll_dice():
    return random.randint(1, 6)

while True:
    input("Press Enter to roll the dice...")
    print(f"You rolled: {roll_dice()}")
    if input("Roll again? (y/n): ").lower() != 'y':
        break
