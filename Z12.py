#Ерженин Александр ДПИ23-1с

def print_sorted_table(data, key_func, reverse=False):
    # Сортируем список данных с использованием key_func и reverse
    sorted_data = sorted(data, key=key_func, reverse=reverse)
    
    # Печатаем таблицу с результатами
    print(f"{'Фамилия':<15} {'Оценка 1':<10} {'Оценка 2':<10} {'Оценка 3':<10}")
    print("-" * 45)  # Разделительная линия
    
    for row in sorted_data:
        print(f"{row[0]:<15} {row[1]:<10} {row[2]:<10} {row[3]:<10}")

# Пример данных
students = [
    ['Иванов', 3, 5, 4],
    ['Петров', 4, 5, 5],
    ['Сидоров', 3, 3, 3],
    ['Николаев', 4, 4, 3]
]

# Пример сортировки по средней оценке (среднее арифметическое по 3 оценкам)
def average_grade(row):
    return sum(row[1:]) / len(row[1:])

# Пример использования
print("Сортировка по средней оценке по возрастанию:")
print_sorted_table(students, average_grade, reverse=False)

print("\nСортировка по средней оценке по убыванию:")
print_sorted_table(students, average_grade, reverse=True)
