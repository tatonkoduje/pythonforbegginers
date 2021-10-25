person = "Marek Kowalski"
name = person[0:5]
surname = person[6:]
example = person[0:14:2]
example2 = person[::3]
reversed_string = person[::-1]

print(len(person))
print(name)
print(surname)
print(example)
print(example2)
print(reversed_string)

email = "marek.kowalski@google.com"
slice_object = slice(14)
slice_object2 = slice(15, -4)

employee = email[slice_object]
company = email[slice_object2]

print(company)
print("name: " + employee[:5] + ", surname: " + employee[6:] + " from: " + email[15:-4])
