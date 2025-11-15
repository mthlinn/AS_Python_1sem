def zero_between_min_max(lst):
    """
    Обнуляет элементы между минимальным и максимальным элементами
    """
    if len(lst) < 3:
        return lst
    
    # Находим индексы минимального и максимального элементов
    min_index = lst.index(min(lst))
    max_index = lst.index(max(lst))
    
    print(f"Исходный список: {lst}")
    print(f"Минимальный элемент: {lst[min_index]} (индекс {min_index})")
    print(f"Максимальный элемент: {lst[max_index]} (индекс {max_index})")
    
    # Определяем начальный и конечный индексы для обнуления
    start = min(min_index, max_index) + 1
    end = max(min_index, max_index)
    
    print(f"Обнуляем элементы с индекса {start} по {end-1}")
    
    # Обнуляем элементы между min и max
    for i in range(start, end):
        lst[i] = 0
    
    return lst

def main():
    # Тестовые случаи
    test_cases = [
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [3, 1, 4, 1, 5, 9, 2],
        [10, 2, 8, 4, 6],
        [1, 2],
        [5],
        []
    ]
    
    for i, test_list in enumerate(test_cases, 1):
        if len(test_list) == 0:
            continue
            
        print(f"\nТест {i}:")
        original = test_list.copy()
        result = zero_between_min_max(test_list)
        print(f"Результат: {result}")
        
        # Проверка
        min_val = min(original)
        max_val = max(original)
        min_idx = original.index(min_val)
        max_idx = original.index(max_val)
        
        start = min(min_idx, max_idx) + 1
        end = max(min_idx, max_idx)
        
        # Проверяем, что элементы между min и max обнулены
        for j in range(start, end):
            if result[j] != 0:
                print("Ошибка: элемент не обнулен!")
                break
        else:
            print("✓ Проверка пройдена")

if __name__ == "__main__":
    main()
