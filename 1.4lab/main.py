def zero_between_min_max(lst):
    """
    Обнуляет элементы между минимальным и максимальным элементами списка
    """
    if len(lst) < 3:
        print(f"Список слишком короткий: {lst}")
        return lst
    
    print(f"Исходный список: {lst}")
    
    # Находим индексы минимального и максимального элементов
    min_index = lst.index(min(lst))
    max_index = lst.index(max(lst))
    
    print(f"Минимальный элемент: {lst[min_index]} (индекс {min_index})")
    print(f"Максимальный элемент: {lst[max_index]} (индекс {max_index})")
    
    # Определяем начальный и конечный индексы для обнуления
    start_index = min(min_index, max_index) + 1
    end_index = max(min_index, max_index)
    
    print(f"Обнуляем элементы с индекса {start_index} по {end_index - 1}")
    
    # Проверяем, есть ли элементы для обнуления
    if start_index >= end_index:
        print("Нет элементов для обнуления (min и max соседние)")
        return lst
    
    # Обнуляем элементы между min и max
    for i in range(start_index, end_index):
        print(f"Обнуляем элемент с индексом {i}: {lst[i]} -> 0")
        lst[i] = 0
    
    return lst

def main():
    # Тестовые случаи
    test_cases = [
        [1, 2, 3, 4, 5],           # min=1, max=5
        [5, 4, 3, 2, 1],           # min=1, max=5
        [3, 1, 4, 1, 5, 9, 2],     # min=1, max=9
        [10, 2, 8, 4, 6],          # min=2, max=10
        [1, 5, 2],                 # min=1, max=5
        [5, 1],                    # слишком короткий
        [7],                       # слишком короткий
        [1, 1, 1, 1],             # все элементы равны
        [2, 8, 3, 5, 1, 7, 4]     # сложный случай
    ]
    
    print("ОБНУЛЕНИЕ ЭЛЕМЕНТОВ МЕЖДУ MIN И MAX")
    print("=" * 60)
    
    for i, test_list in enumerate(test_cases, 1):
        print(f"\nТест {i}:")
        original = test_list.copy()
        result = zero_between_min_max(test_list)
        print(f"Результат: {result}")
        
        # Проверка корректности
        if len(original) >= 3:
            min_val = min(original)
            max_val = max(original)
            min_idx = original.index(min_val)
            max_idx = original.index(max_val)
            
            start = min(min_idx, max_idx) + 1
            end = max(min_idx, max_idx)
            
            # Проверяем, что элементы между min и max обнулены
            correct = True
            for j in range(start, end):
                if result[j] != 0:
                    correct = False
                    break
            
            print(f"✓ Проверка пройдена: {correct}")
        print("-" * 40)

# Дополнительная функция для разных сценариев
def analyze_different_cases():
    """
    Анализ различных сценариев расположения min и max
    """
    print("\n" + "=" * 60)
    print("АНАЛИЗ РАЗЛИЧНЫХ СЦЕНАРИЕВ")
    print("=" * 60)
    
    cases = [
        ("Min слева, max справа", [1, 2, 3, 4, 5]),
        ("Max слева, min справа", [5, 4, 3, 2, 1]),
        ("Min и max в середине", [10, 1, 8, 9, 2]),
        ("Min и max рядом", [3, 1, 5, 4, 2]),
        ("Несколько min/max", [1, 2, 1, 5, 5, 3])
    ]
    
    for description, test_list in cases:
        print(f"\n{description}: {test_list}")
        original = test_list.copy()
        result = zero_between_min_max(test_list)
        
        # Подсчет обнуленных элементов
        zero_count = sum(1 for x in result if x == 0)
        original_zero_count = sum(1 for x in original if x == 0)
        newly_zeroed = zero_count - original_zero_count
        
        print(f"Обнулено элементов: {newly_zeroed}")
        print(f"Итог: {result}")

if __name__ == "__main__":
    main()
    analyze_different_cases()
