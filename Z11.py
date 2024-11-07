#Ерженин Александр ДПИ23-1с

def get_even_indices(S):
    # Используем enumerate, чтобы получить индексы и элементы
    even_indices = list(map(lambda x: x[0], filter(lambda x: x[1] % 2 == 0, enumerate(S))))
    return even_indices

# Пример использования
S = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Пример списка
even_indices = get_even_indices(S)

print("Индексы четных элементов:", even_indices)
