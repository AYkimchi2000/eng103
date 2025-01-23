print("How many integers would you like to enter?")
loop_counter = int(input())
print(f"Please enter {loop_counter} integers.")
user_input = int(input())
min_value = user_input
max_value = user_input

for i in range(1, loop_counter): 
    user_input = int(input())
    if user_input < min_value:
        min_value = user_input
    if user_input > max_value:
        max_value = user_input

print(f"min: {min_value}")
print(f"max: {max_value}")
