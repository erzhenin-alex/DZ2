#Ерженин Александр ДПИ23-1с

from functools import reduce

# Исходный список целых чисел
numbers = [1, 2, 3, 4, 5]

# Преобразуем каждый элемент списка в строку
str_numbers = map(str, numbers)

# Объединяем элементы с помощью reduce, разделяя пробелами
result_string = reduce(lambda x, y: x + ' ' + y, str_numbers)

print("Строковое представление:", result_string)
