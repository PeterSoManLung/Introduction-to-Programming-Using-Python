# Coding By Peter So
# 利用分鐘找年數

input_min = eval(input("Enter the munber of minutes: "))

one_year_min = (365*(24*60))
one_day_min = 24*60

year = input_min // one_year_min
day = (input_min % one_year_min) // one_day_min
minutes = day // 60

print(input_min, "minutes is approximately", year, "years and", day, "days and", minutes, "minutes")

