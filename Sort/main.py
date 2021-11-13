numbers = [2, 5, 3, 8, 12, 88, 10]

numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)
print("-----------------")


food = ("szynka", "chleb", "woda", "mleko", "ser")
sorted_food = sorted(food, reverse=True)

print(food)
print(sorted_food)
print("-----------------")


food_prices = [("woda", 2), ("chleb", 3), ("ser", 20),  ("szynka", 30),  ("mleko", 4)]

food_prices.sort()
print(food_prices)

food_prices.sort(key=lambda prices: prices[1], reverse=True)
print(food_prices)
