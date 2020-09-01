# Coding By Peter So
def calRectangleArea(width, height):
    print("area =",(width*height))

def main():
    width = eval(input("Rectangle\narea = width x height\nEneter the width\n"))
    height = eval(input("Eneter the height\n"))
    calRectangleArea(width, height)

if __name__ == "__main__":
    main()