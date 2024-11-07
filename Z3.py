#Ерженин Александр ДПИ23-1с

from functools import reduce

# Исходный список с подряд идущими повторяющимися элементами
numbers = [1, 2, 3, 4, 4, 4, 5, 6, 6, 7, 6, 1, 1]

# Используем reduce, чтобы оставить только одно вхождение каждого подряд идущего элемента
unique_numbers = reduce(lambda acc, x: acc + [x] if not acc or acc[-1] != x else acc, numbers, [])

print("Список без подряд идущих повторяющихся элементов:", unique_numbers)
