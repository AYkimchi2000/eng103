target_int = int(input("Please enter a positive integer: "))
print(f"The factors of {target_int} are:")
for i in range(target_int):
    p = i + 1
    if target_int % p == 0:
        print(p)
