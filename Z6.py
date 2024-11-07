#Ерженин Александр ДПИ23-1с

def find_median_element(arr):
    # Сортируем список
    sorted_arr = sorted(arr)
    
    # Находим индекс среднего элемента
    median_index = len(sorted_arr) // 2
    
    # Возвращаем средний элемент
    return sorted_arr[median_index]

# Пример использования
A = [7, 1, 3, 9, 5]  # Список из 2n + 1 = 5 элементов
median_element = find_median_element(A)

print("Средний элемент:", median_element)
