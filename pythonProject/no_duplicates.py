numbers = [1, 4, 4, 4, 3, 3, 6, 6, 5]
unique = []
for number in numbers:
    if number not in unique:
        unique.append(number)
print(unique)