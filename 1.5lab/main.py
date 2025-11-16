def filter_and_sort_numbers(lst, k):
    """
    Выбирает из списка все числа меньше k и сортирует их по возрастанию
    """
    print(f"Исходный список: {lst}")
    print(f"Заданное число k: {k}")
    
    # Шаг 1: Фильтрация - выбираем числа меньше k
    filtered = []
    for num in lst:
        if num < k:
            filtered.append(num)
            print(f"  {num} < {k} → добавляем")
        else:
            print(f"  {num} >= {k} → пропускаем")
    
    print(f"После фильтрации: {filtered}")
    
    # Шаг 2: Сортировка по возрастанию
    if filtered:
        filtered.sort()
        print(f"После сортировки: {filtered}")
    else:
        print("Нет чисел для сортировки")
    
    return filtered

def filter_and_sort_compact(lst, k):
    """
    Компактная версия с использованием list comprehension
    """
    filtered = [x for x in lst if x < k]
    filtered.sort()
    return filtered

def main():
    # Тестовые случаи
    test_cases = [
        ([1, 5, 2, 8, 3, 7, 4], 5),
        ([10, 20, 30, 40, 50], 25),
        ([5, 3, 1, 7, 2, 9], 10),
        ([1, 2, 3, 4, 5], 1),
        ([], 5),
        ([8, 6, 4, 2], 3),
        ([1.5, 2.7, 3.1, 4.9], 3.0),
        ([-3, -1, 0, 2, 4], 1)
    ]
    
    print("ФИЛЬТРАЦИЯ И СОРТИРОВКА ЧИСЕЛ")
    print("=" * 50)
    
    for i, (numbers, k) in enumerate(test_cases, 1):
        print(f"\nТест {i}:")
        result = filter_and_sort_numbers(numbers, k)
        print(f"Результат: {result}")
        
        # Проверка корректности
        if result:
            all_less = all(x < k for x in result)
            is_sorted = all(result[i] <= result[i+1] for i in range(len(result)-1))
            print(f"✓ Все числа < {k}: {all_less}")
            print(f"✓ Отсортировано: {is_sorted}")
        print("-" * 30)

# Функция для анализа различных типов данных
def analyze_different_types():
    """
    Анализ работы с разными типами числовых данных
    """
    print("\n" + "=" * 50)
    print("РАБОТА С РАЗНЫМИ ТИПАМИ ДАННЫХ")
    print("=" * 50)
    
    test_cases = [
        ("Целые числа", [7, 2, 9, 1, 5], 6),
        ("Вещественные числа", [1.1, 2.5, 3.7, 0.5, 4.2], 3.0),
        ("Отрицательные числа", [-5, -2, 0, 3, -1], 0),
        ("Смешанные числа", [1, 2.5, -3, 0, 4.7], 2)
    ]
    
    for description, numbers, k in test_cases:
        print(f"\n{description}: {numbers}, k = {k}")
        result = filter_and_sort_compact(numbers, k)
        print(f"Результат: {result}")

# Функция для демонстрации производительности
def demonstrate_large_dataset():
    """
    Демонстрация работы на большом наборе данных
    """
    print("\n" + "=" * 50)
    print("РАБОТА С БОЛЬШИМ НАБОРОМ ДАННЫХ")
    print("=" * 50)
    
    import random
    
    # Генерируем большой список случайных чисел
    large_list = [random.randint(1, 1000) for _ in range(20)]
    k = 500
    
    print(f"Большой список (20 элементов): {large_list}")
    print(f"k = {k}")
    
    result = filter_and_sort_compact(large_list, k)
    print(f"Найдено чисел < {k}: {len(result)}")
    print(f"Результат: {result}")

if __name__ == "__main__":
    main()
    analyze_different_types()
    demonstrate_large_dataset()
