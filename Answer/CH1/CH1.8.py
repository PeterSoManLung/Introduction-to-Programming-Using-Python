# Coding By Peter So
import math

def calCricleAreaandPerimeter(radius):
    area = (radius**2 * math.pi)
    perimeter = 2 * radius * math.pi

    print("area =", area)
    print("perimeter =", perimeter)

def main():
    radius = eval(input("Cricle\narea = radius x radius x pi\nperimeter = 2 x radius x pi\nprint input radius:\n"))
    calCricleAreaandPerimeter(radius)

if __name__ == "__main__":
    main()