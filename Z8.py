#Ерженин Александр ДПИ23-1с

from functools import reduce

def double_factorial(n):
    # Создаем последовательность нечетных чисел от n до 1
    sequence = range(n, 0, -2)
    
    # Используем reduce для вычисления произведения всех чисел в последовательности
    return reduce(lambda x, y: x * y, sequence)

# Пример использования
n = 7  # Нечетное число
result = double_factorial(n)

print(f"Двойной факториал {n}!! равен {result}")
