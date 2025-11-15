def remove_odd_index_chars(s):
    """
    Удаляет символы с нечетными индексами из строки
    """
    print(f"Исходная строка: '{s}'")
    print(f"Длина строки: {len(s)}")
    
    # Создаем новую строку только с символами на четных индексах
    result = ""
    for i, char in enumerate(s):
        if i % 2 == 0:  # четные индексы (0, 2, 4, ...)
            result += char
            print(f"Индекс {i}: '{char}' → сохраняем")
        else:
            print(f"Индекс {i}: '{char}' → удаляем")
    
    return result

def remove_odd_index_chars_simple(s):
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
        "abcdefghij"
    ]
    
    print("РЕШЕНИЕ ЧЕРЕЗ ЦИКЛ:")
    print("=" * 50)
    
    for i, test_string in enumerate(test_cases, 1):
        print(f"\nТест {i}:")
        result = remove_odd_index_chars(test_string)
        print(f"Результат: '{result}'")
        
        # Проверка через срез
        expected = test_string[::2]
        print(f"Проверка (срез [::2]): '{expected}'")
        print(f"✓ Совпадение: {result == expected}")

    print("\n" + "=" * 50)
    print("ПРОВЕРКА ЧЕРЕЗ СРЕЗЫ:")
    print("=" * 50)
    
    # Демонстрация работы срезов
    examples = ["abcdef", "12345", "Hello"]
    
    for example in examples:
        print(f"\nСтрока: '{example}'")
        print(f"Индексы: {list(range(len(example)))}")
        print(f"Символы: {list(example)}")
        print(f"Срез [::2]: '{example[::2]}'")
        print(f"Результат: '{example[::2]}'")

if __name__ == "__main__":
    main()
