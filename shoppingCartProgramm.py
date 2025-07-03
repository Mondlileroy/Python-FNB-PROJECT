foods = []
prices = []
total = 0

while True:
    food = input("Enter a food product (or type 'exit' to finish): ")
    if food.lower() == 'exit':
        break
    else:
        price = float(input(f"Enter the price of {food}: R"))
        foods.append(food)
        prices.append(price)


print("-----------YOUR SHOPPING CART-----------")
for food in foods:
    print(food)


total = sum(prices)

print("-----------YOUR SHOPPING CART PRICES-----------")
print(f"\nTotal cost of items in the cart: R{total}")
print("Thank you for shopping with us!")
