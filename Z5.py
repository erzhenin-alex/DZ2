#Ерженин Александр ДПИ23-1с

def split_list(A):
    # Сортируем список A
    A_sorted = sorted(A)
    
    # Вычисляем N
    N = len(A_sorted) // 2
    
    # Разбиваем на списки B и C
    B = A_sorted[:N]
    C = A_sorted[N:]
    
    return B, C

# Пример использования
A = [8, 1, 3, 5, 9, 2, 7, 6]  # A состоит из 8 (2N) элементов
B, C = split_list(A)

print("Список B:", B)
print("Список C:", C)
