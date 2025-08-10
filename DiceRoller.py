import random

while True:
    rolls = int(input("How many dice to roll (1 or 2)? "))
    if rolls in [1, 2]:
        result = [random.randint(1, 6) for _ in range(rolls)]
        print("🎲 You rolled:", result)
    else:
        print("❌ Only 1 or 2 allowed.")
    
    if input("Roll again? (y/n): ").lower() != 'y':
        break