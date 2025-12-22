# а) Функция pair_and_filter
def pair_and_filter(list1, list2, filter_function=None):
    """
    Создает список пар элементов (x, y), где x из list1, а y из list2.
    
    Параметры:
    list1, list2: списки элементов
    filter_function: необязательная функция, возвращающая True для пар,
                    которые должны быть включены в результат
    
    Возвращает:
    Список кортежей (x, y), удовлетворяющих условию filter_function,
    или все возможные пары, если filter_function не указана.
    """
    result = []
    
    for x in list1:
        for y in list2:
            # Если filter_function не указана или возвращает True для пары
            if filter_function is None or filter_function(x, y):
                result.append((x, y))
    
    return result


# б) Функция concat_or_upper
def concat_or_upper(strings, uppercase=False):
    """
    Соединяет строки из списка.
    
    Параметры:
    strings: список строк
    uppercase: если True, строки преобразуются в верхний регистр
    
    Возвращает:
    Единую строку с элементами, соединенными пробелом.
    """
    if not strings:
        return ""
    
    # Обрабатываем строки в зависимости от параметра uppercase
    if uppercase:
        processed_strings = [s.upper() for s in strings]
    else:
        processed_strings = strings
    
    # Соединяем строки пробелами
    return " ".join(processed_strings)


# в) Функция filter_uppercase_strings
def filter_uppercase_strings(strings):
    """
    Фильтрует строки, оставляя только те, что полностью состоят из заглавных букв.
    
    Параметры:
    strings: список строк
    
    Возвращает:
    Новый список, содержащий только строки в верхнем регистре.
    """
    result = []
    
    for s in strings:
        # Проверяем, состоит ли строка только из заглавных букв
        if s.isupper():
            result.append(s)
    
    return result


# г) Функция unique_sorted_elements
def unique_sorted_elements(*lists):
    """
    Объединяет элементы из всех переданных списков, удаляет дубликаты и сортирует.
    
    Параметры:
    *lists: произвольное количество списков
    
    Возвращает:
    Отсортированный список уникальных элементов.
    """
    # Собираем все элементы в один список
    all_elements = []
    for lst in lists:
        all_elements.extend(lst)
    
    # Удаляем дубликаты и сортируем
    return sorted(set(all_elements))


# Альтернативные реализации для сравнения
def pair_and_filter_comprehension(list1, list2, filter_function=None):
    """Альтернативная реализация с использованием list comprehension"""
    if filter_function is None:
        return [(x, y) for x in list1 for y in list2]
    else:
        return [(x, y) for x in list1 for y in list2 if filter_function(x, y)]


def filter_uppercase_strings_comprehension(strings):
    """Альтернативная реализация с использованием list comprehension"""
    return [s for s in strings if s.isupper()]


def unique_sorted_elements_set(*lists):
    """Альтернативная реализация с использованием множества и генератора"""
    # Используем генератор для flattening списков
    all_elements = (element for lst in lists for element in lst)
    return sorted(set(all_elements))


# Демонстрационная функция
def demonstrate_functions():
    """Демонстрация работы всех функций"""
    
    print("=" * 70)
    print("ДЕМОНСТРАЦИЯ ВСЕХ ФУНКЦИЙ")
    print("=" * 70)
    
    # а) Демонстрация pair_and_filter
    print("\nа) ФУНКЦИЯ pair_and_filter:")
    print("-" * 40)
    
    list1, list2 = [1, 2], [3, 4]
    
    print(f"list1 = {list1}, list2 = {list2}")
    print(f"pair_and_filter(list1, list2) = {pair_and_filter(list1, list2)}")
    
    # С фильтром (сумма четная)
    filter_func = lambda x, y: (x + y) % 2 == 0
    print(f"pair_and_filter(list1, list2, filter_function=lambda x, y: (x + y) % 2 == 0) = "
          f"{pair_and_filter(list1, list2, filter_function=filter_func)}")
    
    # Дополнительные примеры
    list3, list4 = ['a', 'b'], [1, 2, 3]
    print(f"\nlist3 = {list3}, list4 = {list4}")
    print(f"pair_and_filter(list3, list4) = {pair_and_filter(list3, list4)}")
    
    # Фильтр: только пары, где второй элемент > 1
    filter_func2 = lambda x, y: y > 1
    print(f"pair_and_filter(list3, list4, filter_function=lambda x, y: y > 1) = "
          f"{pair_and_filter(list3, list4, filter_function=filter_func2)}")
    
    # б) Демонстрация concat_or_upper
    print("\n\nб) ФУНКЦИЯ concat_or_upper:")
    print("-" * 40)
    
    strings1 = ['hello', 'world']
    print(f"strings = {strings1}")
    print(f"concat_or_upper(strings) = '{concat_or_upper(strings1)}'")
    print(f"concat_or_upper(strings, uppercase=True) = '{concat_or_upper(strings1, uppercase=True)}'")
    
    strings2 = ['Python', 'is', 'awesome']
    print(f"\nstrings = {strings2}")
    print(f"concat_or_upper(strings) = '{concat_or_upper(strings2)}'")
    print(f"concat_or_upper(strings, uppercase=True) = '{concat_or_upper(strings2, uppercase=True)}'")
    
    # в) Демонстрация filter_uppercase_strings
    print("\n\nв) ФУНКЦИЯ filter_uppercase_strings:")
    print("-" * 40)
    
    test_strings1 = ['HELLO', 'World', 'BYE']
    print(f"strings = {test_strings1}")
    print(f"filter_uppercase_strings(strings) = {filter_uppercase_strings(test_strings1)}")
    
    test_strings2 = ['Python', 'JAVA', 'c++']
    print(f"\nstrings = {test_strings2}")
    print(f"filter_uppercase_strings(strings) = {filter_uppercase_strings(test_strings2)}")
    
    # г) Демонстрация unique_sorted_elements
    print("\n\nг) ФУНКЦИЯ unique_sorted_elements:")
    print("-" * 40)
    
    list_a, list_b, list_c = [3, 1], [2, 3], [1, 4]
    print(f"Списки: {list_a}, {list_b}, {list_c}")
    print(f"unique_sorted_elements(list_a, list_b, list_c) = "
          f"{unique_sorted_elements(list_a, list_b, list_c)}")
    
    list_d, list_e, list_f = ['b', 'a'], ['c', 'a'], ['d', 'b']
    print(f"\nСписки: {list_d}, {list_e}, {list_f}")
    print(f"unique_sorted_elements(list_d, list_e, list_f) = "
          f"{unique_sorted_elements(list_d, list_e, list_f)}")


# Тестирование функций
def run_tests():
    """Тестирование всех функций"""
    
    print("\n" + "=" * 70)
    print("ТЕСТИРОВАНИЕ ФУНКЦИЙ")
    print("=" * 70)
    
    tests_passed = 0
    total_tests = 0
    
    # Тесты для pair_and_filter
    print("\n1. Тестирование pair_and_filter:")
    
    # Тест 1: Без фильтра
    result = pair_and_filter([1, 2], [3, 4])
    expected = [(1, 3), (1, 4), (2, 3), (2, 4)]
    total_tests += 1
    if result == expected:
        print("   ✓ Тест 1 пройден")
        tests_passed += 1
    else:
        print(f"   ✗ Тест 1 не пройден: ожидалось {expected}, получено {result}")
    
    # Тест 2: С фильтром (четная сумма)
    filter_func = lambda x, y: (x + y) % 2 == 0
    result = pair_and_filter([1, 2], [3, 4], filter_function=filter_func)
    expected = [(1, 3), (2, 4)]
    total_tests += 1
    if result == expected:
        print("   ✓ Тест 2 пройден")
        tests_passed += 1
    else:
        print(f"   ✗ Тест 2 не пройден: ожидалось {expected}, получено {result}")
    
    # Тесты для concat_or_upper
    print("\n2. Тестирование concat_or_upper:")
    
    # Тест 1: Без uppercase
    result = concat_or_upper(['hello', 'world'])
    expected = 'hello world'
    total_tests += 1
    if result == expected:
        print("   ✓ Тест 1 пройден")
        tests_passed += 1
    else:
        print(f"   ✗ Тест 1 не пройден: ожидалось '{expected}', получено '{result}'")
    
    # Тест 2: С uppercase=True
    result = concat_or_upper(['hello', 'world'], uppercase=True)
    expected = 'HELLO WORLD'
    total_tests += 1
    if result == expected:
        print("   ✓ Тест 2 пройден")
        tests_passed += 1
    else:
        print(f"   ✗ Тест 2 не пройден: ожидалось '{expected}', получено '{result}'")
    
    # Тесты для filter_uppercase_strings
    print("\n3. Тестирование filter_uppercase_strings:")
    
    # Тест 1
    result = filter_uppercase_strings(['HELLO', 'World', 'BYE'])
    expected = ['HELLO', 'BYE']
    total_tests += 1
    if result == expected:
        print("   ✓ Тест 1 пройден")
        tests_passed += 1
    else:
        print(f"   ✗ Тест 1 не пройден: ожидалось {expected}, получено {result}")
    
    # Тест 2
    result = filter_uppercase_strings(['Python', 'JAVA', 'c++'])
    expected = ['JAVA']
    total_tests += 1
    if result == expected:
        print("   ✓ Тест 2 пройден")
        tests_passed += 1
    else:
        print(f"   ✗ Тест 2 не пройден: ожидалось {expected}, получено {result}")
    
    # Тесты для unique_sorted_elements
    print("\n4. Тестирование unique_sorted_elements:")
    
    # Тест 1: Числа
    result = unique_sorted_elements([3, 1], [2, 3], [1, 4])
    expected = [1, 2, 3, 4]
    total_tests += 1
    if result == expected:
        print("   ✓ Тест 1 пройден")
        tests_passed += 1
    else:
        print(f"   ✗ Тест 1 не пройден: ожидалось {expected}, получено {result}")
    
    # Тест 2: Строки
    result = unique_sorted_elements(['b', 'a'], ['c', 'a'], ['d', 'b'])
    expected = ['a', 'b', 'c', 'd']
    total_tests += 1
    if result == expected:
        print("   ✓ Тест 2 пройден")
        tests_passed += 1
    else:
        print(f"   ✗ Тест 2 не пройден: ожидалось {expected}, получено {result}")
    
    # Итоги тестирования
    print("\n" + "=" * 40)
    print(f"ИТОГИ ТЕСТИРОВАНИЯ: {tests_passed}/{total_tests} тестов пройдено")
    if tests_passed == total_tests:
        print("✓ Все тесты успешно пройдены!")
    else:
        print(f"✗ Не пройдено {total_tests - tests_passed} тестов")


# Примеры использования в реальных сценариях
def practical_examples():
    """Практические примеры использования функций"""
    
    print("\n" + "=" * 70)
    print("ПРАКТИЧЕСКИЕ ПРИМЕРЫ")
    print("=" * 70)
    
    # Пример 1: Генерация таблицы умножения с фильтрацией
    print("\n1. Генерация таблицы умножения (только четные результаты):")
    numbers = list(range(1, 6))
    
    # Фильтр: произведение кратно 2
    filter_mult = lambda x, y: (x * y) % 2 == 0
    
    multiplication_pairs = pair_and_filter(numbers, numbers, filter_function=filter_mult)
    print(f"   Числа: {numbers}")
    print(f"   Пары с четным произведением:")
    for x, y in multiplication_pairs[:10]:  # Показываем только первые 10 пар
        print(f"   {x} × {y} = {x*y}")
    
    # Пример 2: Обработка текста
    print("\n2. Обработка списка предложений:")
    sentences = [
        "Hello world",
        "PYTHON programming",
        "Data SCIENCE",
        "TEST CASE"
    ]
    
    # Разбиваем предложения на слова
    all_words = []
    for sentence in sentences:
        words = sentence.split()
        all_words.extend(words)
    
    print(f"   Все слова: {all_words}")
    print(f"   Слова в верхнем регистре: {filter_uppercase_strings(all_words)}")
    print(f"   Объединенные слова (верхний регистр): '{concat_or_upper(all_words, uppercase=True)}'")
    
    # Пример 3: Объединение данных из разных источников
    print("\n3. Объединение данных из разных списков:")
    
    # Предположим, у нас есть данные из разных источников
    source1 = ['user1', 'user3', 'user5']
    source2 = ['user2', 'user3', 'user4']
    source3 = ['user1', 'user5', 'user6']
    
    all_users = unique_sorted_elements(source1, source2, source3)
    print(f"   Источник 1: {source1}")
    print(f"   Источник 2: {source2}")
    print(f"   Источник 3: {source3}")
    print(f"   Все уникальные пользователи: {all_users}")
    
    # Пример 4: Создание комбинаций товаров
    print("\n4. Создание комбинаций товаров для акции:")
    products = ['яблоки', 'бананы', 'апельсины']
    discounts = ['10%', '20%', '30%']
    
    # Фильтр: не сочетать бананы со скидкой 30%
    filter_combos = lambda product, discount: not (product == 'бананы' and discount == '30%')
    
    combos = pair_and_filter(products, discounts, filter_function=filter_combos)
    print(f"   Товары: {products}")
    print(f"   Скидки: {discounts}")
    print(f"   Возможные комбинации (исключая 'бананы + 30%'):")
    for product, discount in combos:
        print(f"   - {product} со скидкой {discount}")


# Интерактивный режим
def interactive_mode():
    """Интерактивный режим для тестирования функций"""
    
    print("\n" + "=" * 70)
    print("ИНТЕРАКТИВНЫЙ РЕЖИМ")
    print("=" * 70)
    
    while True:
        print("\nВыберите функцию для тестирования:")
        print("1. pair_and_filter - создание пар с фильтрацией")
        print("2. concat_or_upper - объединение строк")
        print("3. filter_uppercase_strings - фильтрация строк в верхнем регистре")
        print("4. unique_sorted_elements - объединение и сортировка списков")
        print("0. Выход")
        
        choice = input("\nВаш выбор: ").strip()
        
        if choice == '0':
            print("Выход из интерактивного режима...")
            break
        
        elif choice == '1':
            print("\nТестирование pair_and_filter:")
            try:
                list1 = eval(input("Введите первый список (например, [1, 2, 3]): "))
                list2 = eval(input("Введите второй список (например, ['a', 'b']): "))
                filter_input = input("Введите фильтрующую функцию (или оставьте пустым): ").strip()
                
                if filter_input:
                    filter_func = eval(filter_input)
                    result = pair_and_filter(list1, list2, filter_function=filter_func)
                else:
                    result = pair_and_filter(list1, list2)
                
                print(f"\nРезультат: {result}")
                
            except Exception as e:
                print(f"Ошибка: {e}")
        
        elif choice == '2':
            print("\nТестирование concat_or_upper:")
            try:
                strings_input = input("Введите список строк (например, ['hello', 'world']): ")
                strings = eval(strings_input)
                uppercase_input = input("Преобразовать в верхний регистр? (y/n): ").strip().lower()
                
                uppercase = uppercase_input == 'y'
                result = concat_or_upper(strings, uppercase=uppercase)
                
                print(f"\nРезультат: '{result}'")
                
            except Exception as e:
                print(f"Ошибка: {e}")
        
        elif choice == '3':
            print("\nТестирование filter_uppercase_strings:")
            try:
                strings_input = input("Введите список строк (например, ['HELLO', 'World', 'TEST']): ")
                strings = eval(strings_input)
                result = filter_uppercase_strings(strings)
                
                print(f"\nРезультат: {result}")
                
            except Exception as e:
                print(f"Ошибка: {e}")
        
        elif choice == '4':
            print("\nТестирование unique_sorted_elements:")
            try:
                num_lists = int(input("Сколько списков вы хотите объединить? "))
                lists = []
                
                for i in range(num_lists):
                    lst_input = input(f"Введите список {i+1}: ")
                    lists.append(eval(lst_input))
                
                result = unique_sorted_elements(*lists)
                print(f"\nРезультат: {result}")
                
            except Exception as e:
                print(f"Ошибка: {e}")
        
        else:
            print("Неверный выбор. Попробуйте снова.")


# Основная программа
if __name__ == "__main__":
    print("РЕАЛИЗАЦИЯ ФУНКЦИЙ ДЛЯ РАБОТЫ СО СПИСКАМИ")
    print("=" * 70)
    
    # Демонстрация функций
    demonstrate_functions()
    
    # Тестирование
    run_tests()
    
    # Практические примеры
    practical_examples()
    
    # Интерактивный режим
    interactive_mode()
    
    print("\n" + "=" * 70)
    print("ПРОГРАММА ЗАВЕРШЕНА")
    print("=" * 70)
