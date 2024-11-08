#Ерженин Александр ДПИ23-1с

def split_positive_negative(A3):
    # Отфильтровываем положительные и отрицательные элементы
    B = list(filter(lambda x: x > 0, A3))  # Положительные элементы
    C = list(filter(lambda x: x < 0, A3))  # Отрицательные элементы
    
    return B, C

# Пример использования
A3 = [1, -2, 3, -4, 5, -6, 7, -8]  # Пример списка
B, C = split_positive_negative(A3)

print("Список B (положительные):", B)
print("Список C (отрицательные):", C)
