set1_input = input("Введіть 10 чисел для першої множини через пробіл: ")
set2_input = input("Введіть 10 чисел для другої множини через пробіл: ")

set1 = set(map(int, set1_input.split()))
set2 = set(map(int, set2_input.split()))

print("Множина 1:", set1)
print("Множина 2:", set2)

print("Спільні елементи:", set1 & set2)
print("Різниця (1 - 2):", set1 - set2)
print("Об'єднання:", set1 | set2)