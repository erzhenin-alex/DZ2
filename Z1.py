#Ерженин Александр ДПИ23-1с

from functools import reduce

# Создаем список чисел от 1 до 10
numbers = list(range(1, 11))

# Возводим числа в квадрат с помощью map
squared_numbers = list(map(lambda x: x ** 2, numbers))

# Отфильтровываем четные числа
odd_squares = list(filter(lambda x: x % 2 != 0, squared_numbers))

# Считаем сумму нечетных квадратов с помощью reduce
sum_of_odd_squares = reduce(lambda x, y: x + y, odd_squares)

print("Квадраты чисел от 1 до 10:", squared_numbers)
print("Квадраты нечетных чисел:", odd_squares)
print("Сумма квадратов нечетных чисел:", sum_of_odd_squares)