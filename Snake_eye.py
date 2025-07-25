import random

while True:
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2

    print(f"You rolled {die1} and {die2} (Total: {total})")

    if total == 2:
        print("Snake Eyes! Keep rolling the dice...")
    else:
        print("You didn't roll Snake Eyes. Game over.")
        break



