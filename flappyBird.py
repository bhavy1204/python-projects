import os
import time
import random
import msvcrt

# Game variables
width, height = 30, 15
bird_x, bird_y = 5, height // 2
pipes = []
score = 0
game_over = False

def spawn_pipe():
    gap_y = random.randint(3, height - 4)
    pipes.append([width - 1, gap_y])

def draw():
    os.system("cls")  # "cls" for Windows, "clear" for Linux/Mac
    for y in range(height):
        row = ""
        for x in range(width):
            if x == bird_x and y == bird_y:
                row += "O"
            elif is_pipe(x, y):
                row += "|"
            else:
                row += " "
        print(row)
    print("Score:", score)

def is_pipe(x, y):
    for pipe in pipes:
        px, gap_y = pipe
        if x == px:
            if not (gap_y <= y <= gap_y + 3):
                return True
    return False

def check_collision():
    global game_over
    if bird_y < 0 or bird_y >= height:
        game_over = True
    for pipe in pipes:
        if pipe[0] == bird_x:
            if not (pipe[1] <= bird_y <= pipe[1] + 3):
                game_over = True

# First pipe
spawn_pipe()

# Game loop
while not game_over:
    draw()

    # Input handling (non-blocking)
    if msvcrt.kbhit():
        key = msvcrt.getch()
        if key == b" ":
            bird_y -= 2
    else:
        bird_y += 1  # gravity

    # Move pipes
    for pipe in pipes:
        pipe[0] -= 1

    # Remove off-screen pipes and add new ones
    if pipes and pipes[0][0] < 0:
        pipes.pop(0)
        spawn_pipe()
        score += 1

    check_collision()
    time.sleep(0.1)  # game speed

print("\nGame Over! Final Score:", score)
