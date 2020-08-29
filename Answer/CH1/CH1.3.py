def printF(time):
    for x in range(time):
        print("F", end='')

def printU(time):
    for x in range(time):
        print("U", end='')

def printN(time):
    for x in range(time):
        print("N", end='')

def printSpace(time):
    for x in range(time):
        print(" ", end='')

def main():
    printF(7)
    printSpace(2)
    printU(1)
    printSpace(5)
    printU(1)
    printSpace(2)
    printN(2)
    printSpace(4)
    printN(2)

    print("")
    printF(2)
    printSpace(7)
    printU(1)
    printSpace(5)
    printU(1)
    printSpace(2)
    printN(3)
    printSpace(3)
    printN(2)

    print("")
    printF(7)
    printSpace(2)
    printU(1)
    printSpace(5)
    printU(1)
    printSpace(2)
    printN(2)
    printSpace(1)
    printN(1)
    printSpace(2)
    printN(2)

    print("")
    printF(2)
    printSpace(8)
    printU(1)
    printSpace(3)
    printU(1)
    printSpace(3)
    printN(2)
    printSpace(2)
    printN(1)
    printSpace(1)
    printN(2)

    print("")
    printF(2)
    printSpace(9)
    printU(3)
    printSpace(4)
    printN(2)
    printSpace(3)
    printN(3)

    print("")

if __name__ == "__main__":
    main()