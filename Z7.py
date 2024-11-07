#Ерженин Александр ДПИ23-1с

def get_sorted_indices(arr):
    # Создаем список кортежей (значение, индекс)
    indexed_arr = [(value, index) for index, value in enumerate(arr)]
    
    # Сортируем список кортежей по значению
    indexed_arr.sort()
    
    # Извлекаем только индексы из отсортированного списка
    sorted_indices = [index for _, index in indexed_arr]
    
    return sorted_indices

# Пример использования
A = [7, 1, 3, 9, 5]  # Пример списка
sorted_indices = get_sorted_indices(A)

print("Индексы для возрастающей последовательности:", sorted_indices)
