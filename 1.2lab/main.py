def find_product(A, B):
    """
    Находит произведение всех целых чисел от A до B включительно
    """
    # Проверка условия A < B
    if A >= B:
        return "Ошибка: A должно быть меньше B"
    
    product = 1
    numbers = []
    
    # Вычисляем произведение
    for i in range(A, B + 1):
        product *= i
        numbers.append(i)
    
    # Вывод процесса вычисления
    print(f"Числа от {A} до {B}: {numbers}")
    print(f"Количество чисел: {len(numbers)}")
    
    # Форматируем вычисление для вывода
    calculation = " × ".join(map(str, numbers))
    
    print(f"Вычисление: {calculation} = {product}")
    
    return product

def main():
    # Тестовые примеры
    test_cases = [
        (1, 5),    # 1 × 2 × 3 × 4 × 5 = 120
        (2, 6),    # 2 × 3 × 4 × 5 × 6 = 720
        (3, 7),    # 3 × 4 × 5 × 6 × 7 = 2520
        (-3, 2),   # -3 × -2 × -1 × 0 × 1 × 2 = 0
        (5, 8)     # 5 × 6 × 7 × 8 = 1680
    ]
    
    print("ПРОИЗВЕДЕНИЕ ЧИСЕЛ ОТ A ДО B")
    print("=" * 50)
    
    for A, B in test_cases:
        print(f"\nA = {A}, B = {B}:")
        result = find_product(A, B)
        print(f"Результат: {result}")
        print("-" * 30)

# Дополнительная функция с проверкой особых случаев
def product_with_checks(A, B):
    """
    Версия с проверкой особых случаев
    """
    if A >= B:
        return "Ошибка: A должно быть строго меньше B"
    
    # Если диапазон включает 0, произведение будет 0
    if A <= 0 <= B:
        return 0
    
    product = 1
    for i in range(A, B + 1):
        product *= i
    
    return product

# Проверка на конкретных значениях
def specific_example():
    print("\n" + "=" * 50)
    print("КОНКРЕТНЫЙ ПРИМЕР")
    print("=" * 50)
    
    A = 4
    B = 8
    result = find_product(A, B)
    
    print(f"\nПроверка: 4 × 5 × 6 × 7 × 8 = {4*5*6*7*8}")
    print(f"Результат функции: {result}")
    print(f"Совпадение: {result == 4*5*6*7*8}")

if __name__ == "__main__":
    main()
    specific_example()
