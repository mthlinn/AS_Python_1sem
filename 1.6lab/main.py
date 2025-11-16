def remove_odd_index_chars(s):
    """
    Удаляет символы с нечетными индексами из строки
    """
    print(f"Исходная строка: '{s}'")
    print(f"Длина строки: {len(s)}")
    
    result = ""
    for i, char in enumerate(s):
        if i % 2 == 0:  # четные индексы (0, 2, 4, ...)
            result += char
            print(f"Индекс {i}: '{char}' → сохраняем")
        else:
            print(f"Индекс {i}: '{char}' → удаляем")
    
    return result

def remove_odd_index_chars_slice(s):
    """
    Упрощенная версия через срез
    """
    return s[::2]

def main():
    # Тестовые случаи
    test_cases = [
        "Hello World",
        "Python",
        "Programming",
        "A",
        "",
        "123456789",
        "abcdefghij",
        "Привет мир"
    ]
    
    print("УДАЛЕНИЕ СИМВОЛОВ С НЕЧЕТНЫМИ ИНДЕКСАМИ")
    print("=" * 60)
    
    for i, test_string in enumerate(test_cases, 1):
        print(f"\nТест {i}:")
        result = remove_odd_index_chars(test_string)
        print(f"Результат: '{result}'")
        
        # Проверка через срез
        expected = remove_odd_index_chars_slice(test_string)
        print(f"Проверка (срез [::2]): '{expected}'")
        print(f"✓ Совпадение: {result == expected}")

def demonstrate_slice_notation():
    """
    Демонстрация работы срезов
    """
    print("\n" + "=" * 60)
    print("ОБЪЯСНЕНИЕ СРЕЗА [::2]")
    print("=" * 60)
    
    examples = ["abcdef", "12345", "Hello World"]
    
    for example in examples:
        print(f"\nСтрока: '{example}'")
        print(f"Индексы: {list(range(len(example)))}")
        print(f"Символы: {list(example)}")
        print(f"Срез [::2]: '{example[::2]}'")
        print("Синтаксис [start:end:step]:")
        print("  start: не указан (начало)")
        print("  end: не указан (конец)")
        print("  step: 2 (каждый второй символ)")

def analyze_special_cases():
    """
    Анализ особых случаев
    """
    print("\n" + "=" * 60)
    print("АНАЛИЗ ОСОБЫХ СЛУЧАЕВ")
    print("=" * 60)
    
    special_cases = [
        ("Пустая строка", ""),
        ("Один символ", "X"),
        ("Два символа", "AB"),
        ("Три символа", "ABC"),
        ("С пробелами", "A B C D E"),
        ("Спецсимволы", "a@b#c$d%e^")
    ]
    
    for description, test_string in special_cases:
        print(f"\n{description}: '{test_string}'")
        result = test_string[::2]
        print(f"Результат: '{result}'")
        
        # Показываем какие символы сохранились
        if test_string:
            indices = list(range(len(test_string)))
            kept_indices = [i for i in indices if i % 2 == 0]
            kept_chars = [test_string[i] for i in kept_indices]
            print(f"Сохраненные индексы: {kept_indices}")
            print(f"Сохраненные символы: {kept_chars}")

if __name__ == "__main__":
    main()
    demonstrate_slice_notation()
    analyze_special_cases()
