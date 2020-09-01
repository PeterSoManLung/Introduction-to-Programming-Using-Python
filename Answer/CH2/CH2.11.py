# Coding By Peter So
# 計投資總額

final_account_value = eval(input("Enter final account value: "))
annual_interest_rate = eval(input("Enter annual interest rate in percent: "))
years = eval(input("Enter number of years: "))

month = years * 12
monthly_interest_rate = annual_interest_rate / 12


print("Initial deposit value is", ((final_account_value) / ((1 + monthly_interest_rate)**month)))