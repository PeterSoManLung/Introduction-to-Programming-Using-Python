# Coding By Peter So
num = 0
for x in range(1,10):
    if x == 9:
        print(str(x) + " = ", end='')
    else:
        print(str(x) + " + ", end='')
    num += x

print(num)