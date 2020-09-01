# Coding By Peter So
print("a", end='')
for x in range(6):
    print(" ", end="")
print("a^2", end='')
for x in range(5):
    print(" ", end="")
print("a^3")

for x in range(4):
    num = x + 1
    print(num, end="")
    for space in range(6):
        print(" ", end="")
    print(num**2, end="")
    if x == 3:
        for x in range(6):
            print(" ", end="")
    else:
        for x in range(7):
            print(" ", end="")
    print(num**3)
