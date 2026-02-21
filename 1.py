nums = input("Введіть числа через пробіл: ")

numbers = nums.split()
numbers = list(map(int, numbers))

unique_numbers = set(numbers)

print("Унікальні елементи:", unique_numbers)