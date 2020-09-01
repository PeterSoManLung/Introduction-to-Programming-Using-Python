# Coding By Peter So
# Find the length of track

v, a = eval(input("Find the length of track\nFormula: v^2 / 2a\nUsing this format to enter speed and acceleration: speed, acceleration\nEnter Speed and Acceleration: "))

print("The minimum runway length for this airplane is", round(((v**2) / (2*a)), 3), "meters")