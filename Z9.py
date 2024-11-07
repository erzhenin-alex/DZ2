#Ерженин Александр ДПИ23-1с

from functools import reduce

def double_factorial(n):
    # Создаем последовательность четных чисел от n до 2
    sequence = range(n, 1, -2)
    
    # Используем reduce для вычисления произведения всех чисел в последовательности
    return reduce(lambda x, y: x * y, sequence)

# Пример использования
n = 8  # Четное число
result = double_factorial(n)

print(f"Двойной факториал {n}!! равен {result}")
