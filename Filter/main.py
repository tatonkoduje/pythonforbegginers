food = [("szynka", 30, 500), ("chleb", 3, 250), ("ser", 20, 1000), ("mleko", 5, 900), ("woda", 2, 1500)]


def check_cheap(data):
    return data[1] < 20


cheap_food = list(filter(check_cheap, food))
print(cheap_food)

