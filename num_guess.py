print("Enter the integer for the player to guess.")
target = int(input())
print("Enter your guess.")
counter = 0
while True: 
    counter += 1
    guess = int(input())
    if guess == target:
        print(f"You guessed it in {counter} tries.")
        break
    if guess >= target: 
        print("Too high - try again:")
        continue
    if guess <= target:
        print("Too low - try again:")
        continue
