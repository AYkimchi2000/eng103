print("How many integers would you like to enter?")
loop_counter = int(input())
print(f"Please enter {loop_counter} integers.")
min = 0
max = 0
while True:
    if loop_counter == 0:
        break
    user_input = int(input())
    loop_counter -= 1
    if user_input >= max:
        max = user_input
    if user_input <= min:
        min = user_input

print(f"min: {min}")
print(f"max: {105}")