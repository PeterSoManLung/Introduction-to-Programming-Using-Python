# 計貼士

subtotal, gratuity_rate = eval(input("Eneter the subtotal and a gratuity rate: "))

gratuity = subtotal * (gratuity_rate / 100)
total = subtotal + gratuity

print("The gratuity is", round(gratuity,2), "and the total is", round(total,2))