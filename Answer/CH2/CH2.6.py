# 將一個整數的每一個位加總

number = eval(input("Enter the number between 0 and 1000: "))
result = 0

while True:
    if number%10 == 0:
        number //= 10
        result += 0
    else:
        if number // 10 == 0:
            result += number % 10 
            break
        else:
            result += number%10
            number //= 10 

print("The sum of digits is", result)