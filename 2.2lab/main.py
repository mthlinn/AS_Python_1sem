def InvertDigits(K):
    """
    Меняет порядок следования цифр целого положительного числа K на обратный.
    
    Параметры:
    K (int): целое положительное число
    
    Возвращает:
    int: число с обратным порядком цифр
    
    Примеры:
    >>> InvertDigits(12345)
    54321
    >>> InvertDigits(100)
    1
    >>> InvertDigits(7)
    7
    """
    # Проверка на положительное число
    if not isinstance(K, int):
        raise TypeError("K должно быть целым числом")
    
    if K < 0:
        raise ValueError("K должно быть положительным числом")
    
    # Обработка особого случая: число 0
    if K == 0:
        return 0
    
    # Способ 1: Математический подход (рекомендуемый)
    inverted_number = 0
    original_number = K
    
    while original_number > 0:
        # Получаем последнюю цифру
        last_digit = original_number % 10
        # Увеличиваем разрядность текущего результата и добавляем цифру
        inverted_number = inverted_number * 10 + last_digit
        # Убираем последнюю цифру из исходного числа
        original_number = original_number // 10
    
    return inverted_number


def InvertDigits_string_method(K):
    """
    Альтернативная реализация с использованием строк (менее эффективна для больших чисел).
    """
    # Проверка на положительное число
    if not isinstance(K, int):
        raise TypeError("K должно быть целым числом")
    
    if K < 0:
        raise ValueError("K должно быть положительным числом")
    
    # Преобразуем число в строку, разворачиваем и преобразуем обратно
    return int(str(K)[::-1])


def InvertDigits_recursive(K):
    """
    Рекурсивная реализация функции.
    """
    # Базовый случай: число меньше 10
    if K < 10:
        return K
    
    # Рекурсивный случай
    last_digit = K % 10
    remaining_digits = K // 10
    
    # Находим количество цифр в оставшейся части
    digit_count = len(str(remaining_digits))
    
    # Помещаем последнюю цифру на первую позицию
    return last_digit * (10 ** digit_count) + InvertDigits_recursive(remaining_digits)


def demonstrate_invert_digits():
    """Демонстрация работы функции InvertDigits"""
    
    print("=" * 50)
    print("ДЕМОНСТРАЦИЯ ФУНКЦИИ InvertDigits")
    print("=" * 50)
    
    test_cases = [
        (12345, 54321),
        (100, 1),
        (7, 7),
        (987654321, 123456789),
        (102030, 30201),
        (1234567890, 987654321),
        (1010101, 1010101),  # Палиндром
        (2468, 8642),
    ]
    
    print("\nТестирование основной функции:")
    print("-" * 40)
    print(f"{'Исходное число':<15} {'Результат':<15} {'Ожидаемый':<15} {'Статус':<10}")
    print("-" * 40)
    
    for original, expected in test_cases:
        result = InvertDigits(original)
        status = "✓" if result == expected else "✗"
        print(f"{original:<15} {result:<15} {expected:<15} {status:<10}")
    
    # Сравнение всех методов
    print("\n\nСравнение всех методов реализации:")
    print("-" * 50)
    
    comparison_numbers = [12345, 100, 987654321]
    
    for num in comparison_numbers:
        print(f"\nЧисло: {num}")
        print(f"Математический метод: {InvertDigits(num)}")
        print(f"Строковый метод: {InvertDigits_string_method(num)}")
        print(f"Рекурсивный метод: {InvertDigits_recursive(num)}")
    
    # Обработка исключений
    print("\n\nПроверка обработки ошибок:")
    print("-" * 30)
    
    error_cases = [
        ("не число", TypeError),
        (-123, ValueError),
        (123.45, TypeError),
    ]
    
    for case, error_type in error_cases:
        try:
            print(f"Попытка: {case} -> ", end="")
            result = InvertDigits(case)
            print(result)
        except Exception as e:
            print(f"Ошибка: {type(e).__name__} - {e}")


def interactive_mode():
    """Интерактивный режим для пользователя"""
    
    print("\n" + "=" * 50)
    print("ИНТЕРАКТИВНЫЙ РЕЖИМ")
    print("=" * 50)
    
    while True:
        print("\nВведите целое положительное число (или 'q' для выхода):")
        user_input = input(">>> ").strip()
        
        if user_input.lower() == 'q':
            print("Выход из программы...")
            break
        
        try:
            number = int(user_input)
            
            if number < 0:
                print("Ошибка: число должно быть положительным!")
                continue
            
            inverted = InvertDigits(number)
            
            print(f"\nРезультат:")
            print(f"Исходное число: {number}")
            print(f"Обратный порядок: {inverted}")
            print(f"Длина числа: {len(str(number))} цифр")
            
            # Дополнительная информация
            if number == inverted:
                print("Замечание: Это число-палиндром!")
            
            # Показать процесс
            print("\nПроцесс разворота по шагам:")
            temp = number
            steps = []
            while temp > 0:
                digit = temp % 10
                steps.append(str(digit))
                temp = temp // 10
            
            print(f"Цифры в обратном порядке: {' → '.join(steps)}")
            
        except ValueError:
            print("Ошибка: введите корректное целое число!")
        except Exception as e:
            print(f"Неожиданная ошибка: {e}")


def performance_test():
    """Тест производительности разных методов"""
    
    print("\n" + "=" * 50)
    print("ТЕСТ ПРОИЗВОДИТЕЛЬНОСТИ")
    print("=" * 50)
    
    import time
    
    test_number = 12345678901234567890
    iterations = 10000
    
    methods = [
        ("Математический", InvertDigits),
        ("Строковый", InvertDigits_string_method),
        ("Рекурсивный", InvertDigits_recursive),
    ]
    
    print(f"\nТестируем на числе: {test_number}")
    print(f"Количество итераций: {iterations:,}")
    print("-" * 50)
    
    for name, func in methods:
        start_time = time.time()
        
        for _ in range(iterations):
            func(test_number)
        
        end_time = time.time()
        elapsed = end_time - start_time
        
        print(f"{name:<15} {elapsed:.6f} секунд ({elapsed/iterations*1e6:.2f} мкс на операцию)")


def additional_features():
    """Дополнительные возможности"""
    
    print("\n" + "=" * 50)
    print("ДОПОЛНИТЕЛЬНЫЕ ВОЗМОЖНОСТИ")
    print("=" * 50)
    
    # 1. Найти все числа-палиндромы в диапазоне
    print("\n1. Числа-палиндромы от 1 до 1000:")
    palindromes = []
    for i in range(1, 1000):
        if i == InvertDigits(i):
            palindromes.append(i)
    
    print(f"   Найдено {len(palindromes)} чисел-палиндромов")
    print(f"   Примеры: {palindromes[:10]}...")
    
    # 2. Числа, которые при обращении дают простое число
    print("\n2. Числа, обращение которых является простым числом:")
    
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    prime_reverses = []
    for i in range(10, 100):
        reversed_i = InvertDigits(i)
        if is_prime(reversed_i):
            prime_reverses.append(i)
    
    print(f"   Примеры (10-99): {prime_reverses[:15]}...")
    
    # 3. Самый большой результат для N-значных чисел
    print("\n3. Максимальный результат разворота для N-значных чисел:")
    for n in range(1, 7):
        max_n_digit = 10**n - 1
        reversed_max = InvertDigits(max_n_digit)
        print(f"   {n}-значное: {max_n_digit} → {reversed_max}")


# Основная программа
if __name__ == "__main__":
    print("ФУНКЦИЯ InvertDigits - РАЗВОРОТ ЧИСЛА")
    print("=" * 50)
    
    # Демонстрация работы
    demonstrate_invert_digits()
    
    # Тест производительности
    performance_test()
    
    # Дополнительные возможности
    additional_features()
    
    # Интерактивный режим
    interactive_mode()
    
    print("\n" + "=" * 50)
    print("ПРОГРАММА ЗАВЕРШЕНА")
    print("=" * 50)
