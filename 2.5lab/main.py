def Digits(S):
    # Базовый случай: если строка пустая
    if len(S) == 0:
        return 0
    
    # Проверяем первый символ
    first_char = S[0]
    
    # Если первый символ - цифра, добавляем 1 и рекурсивно обрабатываем остаток строки
    if first_char.isdigit():
        return 1 + Digits(S[1:])
    else:
        # Если не цифра, просто обрабатываем остаток строки
        return Digits(S[1:])

# Пример использования
if __name__ == "__main__":
    # Тестовые примеры
    test_strings = [
        "Hello123World456",  # 6 цифр
        "abc",               # 0 цифр
        "1234567890",        # 10 цифр
        "a1b2c3d4",          # 4 цифры
        "",                  # 0 цифр (пустая строка)
        "Test 123 test 45"   # 5 цифр
    ]
    
    for test_str in test_strings:
        count = Digits(test_str)
        print(f"Строка: '{test_str}' -> Количество цифр: {count}")
    
    # Для ввода пользователя
    user_input = input("\nВведите строку для проверки: ")
    result = Digits(user_input)
    print(f"Количество цифр в строке: {result}")
