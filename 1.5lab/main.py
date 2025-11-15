def filter_and_sort_numbers(lst, k):
    """
    Выбирает из списка все числа меньше k и сортирует их по возрастанию
    """
    print(f"Исходный список: {lst}")
    print(f"Заданное число k: {k}")
    
    # Выбираем числа меньше k
    filtered_numbers = [x for x in lst if x < k]
    print(f"Числа меньше {k}: {filtered_numbers}")
    
    # Сортируем по возрастанию
    filtered_numbers.sort()
    
    return filtered_numbers

def main():
    # Тестовые случаи
    test_cases = [
        ([1, 5, 2, 8, 3, 7, 4], 5),
        ([10, 20, 30, 40, 50], 25),
        ([5, 3, 1, 7, 2, 9], 10),
        ([1, 2, 3, 4, 5], 1),
        ([], 5),
        ([8, 6, 4, 2], 3),
        ([1.5, 2.7, 3.1, 4.9], 3.0)
    ]
    
    for i, (numbers, k) in enumerate(test_cases, 1):
        print(f"\nТест {i}:")
        result = filter_and_sort_numbers(numbers, k)
        print(f"Результат: {result}")
        
        # Проверка корректности
        if result:
            # Проверяем, что все числа меньше k
            all_less_than_k = all(x < k for x in result)
            # Проверяем, что отсортировано по возрастанию
            is_sorted = all(result[i] <= result[i+1] for i in range(len(result)-1))
            
            print(f"✓ Все числа меньше {k}: {all_less_than_k}")
            print(f"✓ Отсортировано по возрастанию: {is_sorted}")

# Альтернативная реализация с пошаговым выводом
def filter_and_sort_detailed(lst, k):
    """
    Подробная версия с пошаговым выводом
    """
    print(f"\nПодробное решение:")
    print(f"Исходный список: {lst}")
    print(f"Число k: {k}")
    
    # Шаг 1: Фильтрация
    filtered = []
    for num in lst:
        if num < k:
            filtered.append(num)
            print(f"  {num} < {k} → добавляем")
        else:
            print(f"  {num} >= {k} → пропускаем")
    
    print(f"После фильтрации: {filtered}")
    
    # Шаг 2: Сортировка
    if filtered:
        print("Сортировка по возрастанию...")
        filtered.sort()
        print(f"После сортировки: {filtered}")
    else:
        print("Нет чисел для сортировки")
    
    return filtered

if __name__ == "__main__":
    main()
    
    # Демонстрация подробного решения
    print("\n" + "="*50)
    print("ДЕТАЛЬНОЕ РЕШЕНИЕ ДЛЯ ПРИМЕРА")
    print("="*50)
    
    example_list = [7, 2, 9, 1, 5, 3, 8]
    example_k = 6
    filter_and_sort_detailed(example_list, example_k)
