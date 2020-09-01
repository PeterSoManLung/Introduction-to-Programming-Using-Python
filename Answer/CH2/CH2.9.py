# Coding By Peter So
# Wind Chill Effect

fahrenheit = eval(input("Enter the temperature in Fahrenheit between -58 and 41: "))
wind_speed = eval(input("Enter the wind speed in miles per hour: "))

result = (35.74 + 0.6215*fahrenheit) - (35.75 * (wind_speed**0.16)) + (0.4275 * fahrenheit * (wind_speed**0.16))

print("The wind chill index is", round(result,5))