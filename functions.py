thePrice = round(float(input("what is your total price\n")),2)
theDiscount = int(input("what is your discount\n"))

def calculate_discount(price, discount_percent):

    if discount_percent >= 20:
        price *= (1 - (discount_percent / 100))

        return price
    else:
        return round(price, 2)
    

print(f"Your total price is {calculate_discount(thePrice,theDiscount)}")