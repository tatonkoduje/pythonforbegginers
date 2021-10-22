name = "Marek"
age = 18
years = 5

# Operatory arytmetyczne

# +
print(1 + 3)
print(age + years)
# -
print(age - 2)
# *
print(years * 2)
# /
print(age / 3)  # int()
# //
print(age / 7)
print(age // 7)  # Dzieli i zwraca wartość całkowitą ilorazu
# %
print(age % 7)  # Dzieli i zwraca wartość reszty. Bo 7+7 = 14 a 18 - 14 = 4
# **
print(years ** 2)
print(years ** 3)

# niedozwolone operacje
#print(name - 1)
#print(name - name)
#print(name / 2)

# Operatory porównania
minute = 45
hour = 12

# ==
print(minute == hour)
# !=
print(minute != hour)
# <=
print(minute <= hour)
# >=
print(minute >= hour)

# Operatory logiczne

# not
print(not minute < 2)
print(not minute < 50)

# or
print(minute < 2 or hour < 2)
print(minute < 2 or hour < 15)

# and
print(minute < 2 and hour < 2)
print(minute < 2 and hour < 15)
print(minute < 50 and hour < 15)
