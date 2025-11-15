def calculate_product(A, B):
    """
    Вычисляет произведение всех целых чисел от A до B включительно
    """
    # Проверка условий задачи
    if A >= B:
        raise ValueError("Условие задачи: A < B")
    
    # Математическое обоснование:
    # Произведение целых чисел от A до B = A × (A+1) × (A+2) × ... × B
    # Это можно записать как: ∏(i=A to B) i
    
    product = 1
    numbers_sequence = []
    
    # Вычисляем произведение
    for i in range(A, B + 1):
        product *= i
        numbers_sequence.append(i)
    
    return product, numbers_sequence

def calculate_product_optimized(A, B):
    """
    Оптимизированная версия с использованием math.prod (Python 3.8+)
    """
    import math
    return math.prod(range(A, B + 1))

def verify_with_small_example():
    """
    Проверка на маленьком примере для верификации метода
    """
    test_A, test_B = 2, 5
    expected = 2 * 3 * 4 * 5  # 120
    
    result, sequence = calculate_product(test_A, test_B)
    
    print(f"Проверка: A={test_A}, B={test_B}")
    print(f"Числа: {sequence}")
    print(f"Вычисленное произведение: {result}")
    print(f"Ожидаемое произведение: {expected}")
    print(f"Проверка пройдена: {result == expected}")
    
    return result == expected

def analyze_product_properties(A, B):
    """
    Анализ математических свойств произведения
    """
    product, sequence = calculate_product(A, B)
    
    print(f"\nМатематический анализ:")
    print(f"Диапазон: от {A} до {B}")
    print(f"Количество множителей: {len(sequence)}")
    print(f"Произведение можно записать как: ∏(n={A} to {B}) n")
    
    # Проверка на четность/нечетность
    if product % 2 == 0:
        print(f"Произведение ЧЕТНОЕ (содержит четные числа)")
    else:
        print(f"Произведение НЕЧЕТНОЕ (все числа нечетные)")
    
    # Проверка знака
    if product > 0:
        print(f"Произведение ПОЛОЖИТЕЛЬНОЕ")
    elif product < 0:
        print(f"Произведение ОТРИЦАТЕЛЬНОЕ")
    else:
        print(f"Произведение РАВНО НУЛЮ (содержит 0)")
    
    return product

# Основная программа
def main():
    try:
        # Ввод данных
        A = int(input("Введите целое число A: "))
        B = int(input("Введите целое число B (B > A): "))
        
        if A >= B:
            print("Ошибка: A должно быть меньше B")
            return
        
        print("\n" + "="*50)
        print("РЕШЕНИЕ ЗАДАЧИ")
        print("="*50)
        
        # Вычисление произведения
        product, sequence = calculate_product(A, B)
        
        # Вывод результата с математическим обоснованием
        print(f"Дано: A = {A}, B = {B}")
        print(f"Условие: A < B ({A} < {B}) - выполняется")
        print(f"\nЧисла в диапазоне от {A} до {B}: {sequence}")
        
        # Показываем вычисление пошагово
        print(f"\nВычисление произведения:")
        calculation_steps = " × ".join(map(str, sequence))
        print(f"P = {calculation_steps} = {product}")
        
        # Анализ свойств
        analyze_product_properties(A, B)
        
        # Проверка на тестовом примере
        print(f"\nВерификация метода:")
        verify_with_small_example()
        
        print(f"\n" + "="*50)
        print(f"ОТВЕТ: Произведение всех целых чисел от {A} до {B} равно {product}")
        print("="*50)
        
    except ValueError as e:
        print(f"Ошибка ввода: {e}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

# Альтернативное решение с использованием рекурсии (для демонстрации)
def product_recursive(A, B):
    """Рекурсивное вычисление произведения"""
    if A > B:
        return 1
    return A * product_recursive(A + 1, B)

# Запуск программы
if __name__ == "__main__":
    main()
    
    # Демонстрация альтернативных методов
    print(f"\n" + "="*50)
    print("ДОПОЛНИТЕЛЬНЫЕ ПРОВЕРКИ")
    print("="*50)
    
    # Примеры работы
    examples = [(1, 5), (3, 7), (-2, 2)]
    
    for A, B in examples:
        product1, _ = calculate_product(A, B)
        product2 = product_recursive(A, B)
        
        print(f"\nПример: A={A}, B={B}")
        print(f"Итеративный метод: {product1}")
        print(f"Рекурсивный метод: {product2}")
        print(f"Методы дают одинаковый результат: {product1 == product2}")
