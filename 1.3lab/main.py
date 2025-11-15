def calculate_sum(n):
    """
    Вычисляет сумму ряда: 1! - 2! + 3! - ... + (-1)^(n+1) * n!
    """
    if n <= 0:
        return 0
    
    total = 0
    current_factorial = 1
    
    print(f"Вычисление для n = {n}:")
    
    for i in range(1, n + 1):
        # Вычисляем факториал текущего числа
        current_factorial *= i
        
        # Определяем знак: (-1)^(i+1)
        if i % 2 == 1:  # нечетные i: положительный знак
            term = current_factorial
            sign = "+"
        else:  # четные i: отрицательный знак
            term = -current_factorial
            sign = "-"
        
        # Добавляем к общей сумме
        total += term
        
        print(f"Шаг {i}: {sign}{i}! = {sign}{current_factorial} | Сумма: {total}")
    
    return total

def main():
    try:
        n = int(input("Введите натуральное число n: "))
        
        if n <= 0:
            print("Число должно быть натуральным (n > 0)")
            return
        
        result = calculate_sum(n)
        print(f"\nРезультат: {result}")
        
    except ValueError:
        print("Ошибка: введите целое число")

# Проверка на нескольких значениях
def test_cases():
    """
    Тестовые случаи для проверки
    """
    test_values = [1, 2, 3, 4, 5]
    expected_results = [1, -1, 5, -19, 101]
    
    print("Тестовые случаи:")
    for i, n in enumerate(test_values):
        result = calculate_sum(n)
        expected = expected_results[i]
        status = "✓" if result == expected else "✗"
        print(f"n = {n}: получено {result}, ожидалось {expected} {status}")
        print()

if __name__ == "__main__":
    main()
    print("\n" + "="*40)
    test_cases()
