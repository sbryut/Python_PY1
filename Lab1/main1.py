numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
average = sum(filter(None, numbers)) / len(numbers)
index = 0
for element in numbers:
    if element is None:
        break
    index += 1
numbers[index] = average
print("Измененный список:", numbers)
