def merge_dictionaries(dict1, dict2):
    """
    а) Объединяет два словаря в один
    """
    # Способ 1: Использование оператора распаковки (Python 3.5+)
    merged_dict = {**dict1, **dict2}
    
    # Способ 2: Использование метода update()
    # merged_dict = dict1.copy()
    # merged_dict.update(dict2)
    
    # Способ 3: Использование конструктора dict()
    # merged_dict = dict(dict1, **dict2)
    
    return merged_dict

def print_dict_as_table(dictionary):
    """
    б) Выводит содержимое словаря в виде таблицы
    """
    print("Ключ   Значение")
    print("-" * 20)
    
    for key, value in dictionary.items():
        print(f"{key:<7} {value}")
    
    # Альтернативный вариант с более аккуратной таблицей
    print("\nАльтернативный формат:")
    print("-" * 20)
    
    # Определяем максимальную длину ключа для красивого форматирования
    max_key_length = max(len(str(key)) for key in dictionary.keys())
    
    for key, value in dictionary.items():
        print(f"{str(key):<{max_key_length}} : {value}")

def lists_to_dictionary(*lists):
    """
    в) Преобразует несколько списков в словарь
    """
    result = {}
    
    for i, lst in enumerate(lists, 1):
        key = f'key{i}'  # Создаем ключи вида 'key1', 'key2', ...
        result[key] = lst
    
    return result

# Функция для демонстрации всех возможностей
def demonstrate_all_features():
    print("=" * 50)
    print("ДЕМОНСТРАЦИЯ ВСЕХ ФУНКЦИЙ")
    print("=" * 50)
    
    # Примеры данных для тестирования
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'c': 3, 'd': 4}
    dict3 = {'имя': 'Анна', 'возраст': 25, 'город': 'Москва'}
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    list3 = ['яблоко', 'банан', 'апельсин']
    
    # а) Объединение словарей
    print("\n1. ОБЪЕДИНЕНИЕ СЛОВАРЕЙ:")
    print(f"   Словарь 1: {dict1}")
    print(f"   Словарь 2: {dict2}")
    merged = merge_dictionaries(dict1, dict2)
    print(f"   Результат: {merged}")
    
    # б) Вывод словаря в виде таблицы
    print("\n2. ВЫВОД СЛОВАРЯ В ВИДЕ ТАБЛИЦЫ:")
    print_dict_as_table(dict3)
    
    # в) Преобразование списков в словарь
    print("\n3. ПРЕОБРАЗОВАНИЕ СПИСКОВ В СЛОВАРЬ:")
    print(f"   Список 1: {list1}")
    print(f"   Список 2: {list2}")
    print(f"   Список 3: {list3}")
    
    # Вариант 1: Два списка
    dict_from_lists = lists_to_dictionary(list1, list2)
    print(f"   Результат (2 списка): {dict_from_lists}")
    
    # Вариант 2: Три списка
    dict_from_lists = lists_to_dictionary(list1, list2, list3)
    print(f"   Результат (3 списка): {dict_from_lists}")
    
    # г) Комбинированный пример
    print("\n4. КОМБИНИРОВАННЫЙ ПРИМЕР:")
    
    # Объединяем два словаря
    combined_dict = merge_dictionaries({'x': 10, 'y': 20}, {'z': 30})
    print(f"   Объединенный словарь: {combined_dict}")
    
    # Выводим его в виде таблицы
    print("   Табличное представление:")
    print("   " + "-" * 18)
    for key, value in combined_dict.items():
        print(f"   {key:<4} {value}")
    
    # Создаем словарь из списков
    lists_dict = lists_to_dictionary([1, 2], [3, 4, 5], [6])
    print(f"   Словарь из списков: {lists_dict}")

# Дополнительные функции для гибкости
def custom_lists_to_dictionary(lists, keys=None):
    """
    Расширенная версия: позволяет задавать ключи вручную
    """
    if keys is None:
        # Автоматическая генерация ключей
        return lists_to_dictionary(*lists)
    else:
        if len(keys) != len(lists):
            raise ValueError("Количество ключей должно совпадать с количеством списков")
        
        result = {}
        for key, lst in zip(keys, lists):
            result[key] = lst
        return result

def save_dict_to_file(dictionary, filename):
    """
    Дополнительная функция: сохраняет словарь в файл
    """
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("Ключ\tЗначение\n")
        f.write("=" * 30 + "\n")
        for key, value in dictionary.items():
            f.write(f"{key}\t{value}\n")
    print(f"Словарь сохранен в файл: {filename}")

# Основная программа
if __name__ == "__main__":
    # Демонстрация всех возможностей
    demonstrate_all_features()
    
    # Пример использования расширенных функций
    print("\n" + "=" * 50)
    print("ДОПОЛНИТЕЛЬНЫЕ ВОЗМОЖНОСТИ")
    print("=" * 50)
    
    # Использование custom_lists_to_dictionary с пользовательскими ключами
    print("\n1. Преобразование списков с заданными ключами:")
    data_lists = [
        [100, 200, 300],
        ['красный', 'зеленый', 'синий'],
        [True, False, True]
    ]
    
    custom_keys = ['числа', 'цвета', 'флаги']
    custom_dict = custom_lists_to_dictionary(data_lists, custom_keys)
    print(f"   Результат: {custom_dict}")
    
    # Вывод в виде таблицы
    print("\n2. Табличное представление пользовательского словаря:")
    print_dict_as_table(custom_dict)
    
    # Сохранение в файл
    print("\n3. Сохранение словаря в файл:")
    try:
        save_dict_to_file(custom_dict, 'output_dict.txt')
    except Exception as e:
        print(f"   Ошибка при сохранении: {e}")
    
    # Интерактивный режим
    print("\n4. ИНТЕРАКТИВНЫЙ ПРИМЕР:")
    print("   Вы можете протестировать функции самостоятельно:")
    
    # Пример интерактивного ввода
    try:
        # Ввод двух словарей от пользователя
        print("\n   Пример объединения словарей:")
        dict_a = eval(input("   Введите первый словарь (например: {'x': 1, 'y': 2}): "))
        dict_b = eval(input("   Введите второй словарь (например: {'z': 3}): "))
        
        result = merge_dictionaries(dict_a, dict_b)
        print(f"   Результат объединения: {result}")
        
    except:
        print("   Некорректный ввод. Продолжаем демонстрацию...")
    
    print("\n" + "=" * 50)
    print("ПРОГРАММА ЗАВЕРШЕНА")
    print("=" * 50)
