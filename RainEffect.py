
import random
import time
import os

# Characters to rain down (looks more "matrixy" if you add Japanese katakana, etc.)
chars = "01abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ@#$%&*"

def matrix_rain(width=80, height=20, speed=0.05):
    columns = [0] * width  # Track how far each column has "fallen"
    
    try:
        while True:
            os.system("cls" if os.name == "nt" else "clear")
            for y in range(height):
                line = ""
                for x in range(width):
                    if columns[x] == y:
                        line += random.choice(chars)
                        columns[x] = (y + random.randint(1, 10)) % height
                    else:
                        line += " "
                print(line)
            time.sleep(speed)
    except KeyboardInterrupt:
        print("\nMatrix terminated...")

if __name__ == "__main__":
    matrix_rain(width=100, height=30, speed=0.5)
