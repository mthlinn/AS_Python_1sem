def factorial(n):
    """
    Вычисляет факториал числа n
    """
    if n == 0 or n == 1:
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def calculate_series_sum(n):
    """
    Вычисляет сумму ряда: 1! - 2! + 3! - ... + (-1)^(n+1) * n!
    """
    total_sum = 0
    
    print(f"Вычисление суммы для n = {n}:")
    print("Ряд: 1! - 2! + 3! - ... + (-1)^(n+1) * n!")
    print()
    
    for i in range(1, n + 1):
        # Вычисляем факториал
        fact = factorial(i)
        
        # Определяем знак: (-1)^(i+1)
        sign = 1 if i % 2 == 1 else -1
        
        # Текущий член ряда
        term = sign * fact
        
        # Добавляем к общей сумме
        total_sum += term
        
        # Выводим шаг вычисления
        sign_symbol = "+" if sign > 0 else "-"
        print(f"Шаг {i}: {sign_symbol} {i}! = {sign_symbol} {fact} = {term:6d} | Сумма: {total_sum:6d}")
    
    return total_sum

def main():
    # Тестовые случаи
    test_values = [1, 2, 3, 4, 5, 6]
    
    print("ВЫЧИСЛЕНИЕ СУММЫ РЯДА")
    print("=" * 60)
    
    for n in test_values:
        print(f"\nn = {n}:")
        result = calculate_series_sum(n)
        print(f"Финальная сумма: {result}")
        print("-" * 60)

# Альтернативная реализация с оптимизацией
def calculate_series_optimized(n):
    """
    Оптимизированная версия без повторного вычисления факториалов
    """
    total = 0
    current_factorial = 1
    
    print(f"\nОптимизированное вычисление для n = {n}:")
    
    for i in range(1, n + 1):
        current_factorial *= i  # вычисляем i! на основе (i-1)!
        
        sign = 1 if i % 2 == 1 else -1
        term = sign * current_factorial
        total += term
        
        sign_symbol = "+" if sign > 0 else "-"
        print(f"{sign_symbol} {i}! = {sign_symbol} {current_factorial} = {term:6d} | Сумма: {total:6d}")
    
    return total

# Проверка правильности на известных значениях
def verify_results():
    """
    Проверка результатов на известных значениях
    """
    known_results = {
        1: 1,      # 1! = 1
        2: -1,     # 1! - 2! = 1 - 2 = -1
        3: 5,      # 1 - 2 + 6 = 5
        4: -19,    # 1 - 2 + 6 - 24 = -19
        5: 101,    # 1 - 2 + 6 - 24 + 120 = 101
        6: -619    # 1 - 2 + 6 - 24 + 120 - 720 = -619
    }
    
    print("\n" + "=" * 60)
    print("ПРОВЕРКА РЕЗУЛЬТАТОВ")
    print("=" * 60)
    
    for n, expected in known_results.items():
        result1 = calculate_series_sum(n)
        result2 = calculate_series_optimized(n)
        
        print(f"n = {n}: получено {result1}, ожидалось {expected}", 
              "✓" if result1 == expected else "✗")
        print(f"Совпадение методов: {result1 == result2}")
        print()

if __name__ == "__main__":
    main()
    verify_results()
