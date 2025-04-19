import random

num = random.randint(1,10)

for i in range(3):
    guess = int(input("Enter guess between 1-10 : "))
    
    if guess==num:
        print(f" You Won ! the number was : {num}.")
        break
    else:
        print("Bad luck ! try again ")

if guess != num:
     print(f"Sorry you lost the game, The number was {num}")