"""
Модуль vector_operations.py
Функции для работы с числовыми векторами:
1. Сложение векторов
2. Умножение вектора на число
3. Поиск минимального и максимального значений вектора
"""

def vector_addition(vector1, vector2):
    """
    Сложение двух числовых векторов одинаковой длины.
    
    Параметры:
    vector1 (list или tuple): первый вектор
    vector2 (list или tuple): второй вектор
    
    Возвращает:
    list: вектор-сумма
    
    Исключения:
    ValueError: если векторы имеют разную длину
    TypeError: если элементы векторов не являются числами
    
    Пример:
    >>> vector_addition([1, 2, 3], [4, 5, 6])
    [5, 7, 9]
    """
    # Проверка длины векторов
    if len(vector1) != len(vector2):
        raise ValueError(f"Векторы должны иметь одинаковую длину. "
                        f"Получено: {len(vector1)} и {len(vector2)}")
    
    # Проверка типов элементов
    for i, (v1, v2) in enumerate(zip(vector1, vector2)):
        if not (isinstance(v1, (int, float)) and isinstance(v2, (int, float))):
            raise TypeError(f"Элементы векторов должны быть числами. "
                           f"На позиции {i}: {type(v1)} и {type(v2)}")
    
    # Сложение векторов
    result = []
    for v1, v2 in zip(vector1, vector2):
        result.append(v1 + v2)
    
    return result


def vector_scalar_multiplication(vector, scalar):
    """
    Умножение вектора на скаляр (число).
    
    Параметры:
    vector (list или tuple): исходный вектор
    scalar (int или float): скаляр для умножения
    
    Возвращает:
    list: новый вектор, умноженный на скаляр
    
    Исключения:
    TypeError: если элементы вектора не являются числами
               или скаляр не является числом
    
    Пример:
    >>> vector_scalar_multiplication([1, 2, 3], 2)
    [2, 4, 6]
    """
    # Проверка типа скаляра
    if not isinstance(scalar, (int, float)):
        raise TypeError(f"Скаляр должен быть числом. Получено: {type(scalar)}")
    
    # Проверка типа элементов вектора
    for i, value in enumerate(vector):
        if not isinstance(value, (int, float)):
            raise TypeError(f"Элементы вектора должны быть числами. "
                           f"На позиции {i}: {type(value)}")
    
    # Умножение вектора на скаляр
    result = []
    for value in vector:
        result.append(value * scalar)
    
    return result


def vector_min_max(vector):
    """
    Поиск минимального и максимального значений в векторе.
    
    Параметры:
    vector (list или tuple): исходный вектор
    
    Возвращает:
    tuple: (минимальное_значение, максимальное_значение)
    
    Исключения:
    ValueError: если вектор пустой
    TypeError: если элементы вектора не являются числами
    
    Пример:
    >>> vector_min_max([3, 1, 4, 1, 5, 9])
    (1, 9)
    """
    # Проверка, что вектор не пустой
    if not vector:
        raise ValueError("Вектор не должен быть пустым")
    
    # Проверка типа элементов вектора
    for i, value in enumerate(vector):
        if not isinstance(value, (int, float)):
            raise TypeError(f"Элементы вектора должны быть числами. "
                           f"На позиции {i}: {type(value)}")
    
    # Поиск минимального и максимального значений
    min_value = vector[0]
    max_value = vector[0]
    
    for value in vector[1:]:
        if value < min_value:
            min_value = value
        if value > max_value:
            max_value = value
    
    return (min_value, max_value)


# Дополнительные вспомогательные функции
def vector_length(vector):
    """
    Вычисление длины (модуля) вектора.
    
    Параметры:
    vector (list или tuple): исходный вектор
    
    Возвращает:
    float: длина вектора
    
    Пример:
    >>> vector_length([3, 4])
    5.0
    """
    from math import sqrt
    
    # Проверка типа элементов вектора
    for i, value in enumerate(vector):
        if not isinstance(value, (int, float)):
            raise TypeError(f"Элементы вектора должны быть числами. "
                           f"На позиции {i}: {type(value)}")
    
    # Вычисление суммы квадратов
    sum_of_squares = 0
    for value in vector:
        sum_of_squares += value ** 2
    
    return sqrt(sum_of_squares)


def vector_dot_product(vector1, vector2):
    """
    Скалярное произведение двух векторов.
    
    Параметры:
    vector1 (list или tuple): первый вектор
    vector2 (list или tuple): второй вектор
    
    Возвращает:
    float: скалярное произведение
    
    Пример:
    >>> vector_dot_product([1, 2, 3], [4, 5, 6])
    32
    """
    # Проверка длины векторов
    if len(vector1) != len(vector2):
        raise ValueError(f"Векторы должны иметь одинаковую длину. "
                        f"Получено: {len(vector1)} и {len(vector2)}")
    
    # Проверка типов элементов
    for i, (v1, v2) in enumerate(zip(vector1, vector2)):
        if not (isinstance(v1, (int, float)) and isinstance(v2, (int, float))):
            raise TypeError(f"Элементы векторов должны быть числами. "
                           f"На позиции {i}: {type(v1)} и {type(v2)}")
    
    # Вычисление скалярного произведения
    result = 0
    for v1, v2 in zip(vector1, vector2):
        result += v1 * v2
    
    return result


def vector_subtraction(vector1, vector2):
    """
    Вычитание двух векторов.
    
    Параметры:
    vector1 (list или tuple): первый вектор (уменьшаемое)
    vector2 (list или tuple): второй вектор (вычитаемое)
    
    Возвращает:
    list: вектор-разность
    
    Пример:
    >>> vector_subtraction([5, 7, 9], [4, 5, 6])
    [1, 2, 3]
    """
    # Проверка длины векторов
    if len(vector1) != len(vector2):
        raise ValueError(f"Векторы должны иметь одинаковую длину. "
                        f"Получено: {len(vector1)} и {len(vector2)}")
    
    # Проверка типов элементов
    for i, (v1, v2) in enumerate(zip(vector1, vector2)):
        if not (isinstance(v1, (int, float)) and isinstance(v2, (int, float))):
            raise TypeError(f"Элементы векторов должны быть числами. "
                           f"На позиции {i}: {type(v1)} и {type(v2)}")
    
    # Вычитание векторов
    result = []
    for v1, v2 in zip(vector1, vector2):
        result.append(v1 - v2)
    
    return result


def vector_mean(vector):
    """
    Вычисление среднего значения элементов вектора.
    
    Параметры:
    vector (list или tuple): исходный вектор
    
    Возвращает:
    float: среднее значение
    
    Пример:
    >>> vector_mean([1, 2, 3, 4, 5])
    3.0
    """
    # Проверка, что вектор не пустой
    if not vector:
        raise ValueError("Вектор не должен быть пустым")
    
    # Проверка типа элементов вектора
    for i, value in enumerate(vector):
        if not isinstance(value, (int, float)):
            raise TypeError(f"Элементы вектора должны быть числами. "
                           f"На позиции {i}: {type(value)}")
    
    # Вычисление среднего
    return sum(vector) / len(vector)


def normalize_vector(vector):
    """
    Нормализация вектора (приведение к единичной длине).
    
    Параметры:
    vector (list или tuple): исходный вектор
    
    Возвращает:
    list: нормализованный вектор
    
    Пример:
    >>> normalize_vector([3, 4])
    [0.6, 0.8]
    """
    # Вычисление длины вектора
    length = vector_length(vector)
    
    if length == 0:
        raise ValueError("Невозможно нормализовать нулевой вектор")
    
    # Нормализация
    return vector_scalar_multiplication(vector, 1 / length)


# Функция для тестирования модуля
def test_vector_operations():
    """
    Тестирование всех функций модуля.
    
    Возвращает:
    bool: True, если все тесты пройдены успешно
    """
    import math
    
    print("=" * 60)
    print("ТЕСТИРОВАНИЕ МОДУЛЯ VECTOR_OPERATIONS")
    print("=" * 60)
    
    test_results = []
    
    # Тест 1: Сложение векторов
    try:
        result = vector_addition([1, 2, 3], [4, 5, 6])
        expected = [5, 7, 9]
        test_results.append(result == expected)
        print(f"✓ Сложение векторов: {result} == {expected}")
    except Exception as e:
        test_results.append(False)
        print(f"✗ Сложение векторов: ошибка - {e}")
    
    # Тест 2: Умножение вектора на число
    try:
        result = vector_scalar_multiplication([1, 2, 3], 2)
        expected = [2, 4, 6]
        test_results.append(result == expected)
        print(f"✓ Умножение на скаляр: {result} == {expected}")
    except Exception as e:
        test_results.append(False)
        print(f"✗ Умножение на скаляр: ошибка - {e}")
    
    # Тест 3: Поиск min и max
    try:
        result = vector_min_max([3, 1, 4, 1, 5, 9])
        expected = (1, 9)
        test_results.append(result == expected)
        print(f"✓ Min/Max: {result} == {expected}")
    except Exception as e:
        test_results.append(False)
        print(f"✗ Min/Max: ошибка - {e}")
    
    # Тест 4: Длина вектора
    try:
        result = vector_length([3, 4])
        expected = 5.0
        test_results.append(math.isclose(result, expected))
        print(f"✓ Длина вектора: {result} ≈ {expected}")
    except Exception as e:
        test_results.append(False)
        print(f"✗ Длина вектора: ошибка - {e}")
    
    # Тест 5: Скалярное произведение
    try:
        result = vector_dot_product([1, 2, 3], [4, 5, 6])
        expected = 32
        test_results.append(result == expected)
        print(f"✓ Скалярное произведение: {result} == {expected}")
    except Exception as e:
        test_results.append(False)
        print(f"✗ Скалярное произведение: ошибка - {e}")
    
    # Тест 6: Обработка ошибок
    print("\nТестирование обработки ошибок:")
    
    # Неправильная длина векторов
    try:
        vector_addition([1, 2], [1])
        test_results.append(False)
        print("✗ Ожидалось исключение для разных длин векторов")
    except ValueError:
        test_results.append(True)
        print("✓ Корректно обработаны разные длины векторов")
    
    # Нечисловые элементы
    try:
        vector_scalar_multiplication([1, 'a', 3], 2)
        test_results.append(False)
        print("✗ Ожидалось исключение для нечисловых элементов")
    except TypeError:
        test_results.append(True)
        print("✓ Корректно обработаны нечисловые элементы")
    
    # Пустой вектор
    try:
        vector_min_max([])
        test_results.append(False)
        print("✗ Ожидалось исключение для пустого вектора")
    except ValueError:
        test_results.append(True)
        print("✓ Корректно обработан пустой вектор")
    
    # Итоги тестирования
    print("\n" + "=" * 60)
    passed = sum(test_results)
    total = len(test_results)
    
    if all(test_results):
        print(f"✓ ВСЕ ТЕСТЫ ПРОЙДЕНЫ УСПЕШНО ({passed}/{total})")
        return True
    else:
        print(f"✗ ТЕСТИРОВАНИЕ ЗАВЕРШЕНО С ОШИБКАМИ ({passed}/{total})")
        return False


# Пример использования модуля
if __name__ == "__main__":
    print("МОДУЛЬ ДЛЯ РАБОТЫ С ВЕКТОРАМИ")
    print("=" * 60)
    
    # Запуск тестов
    test_passed = test_vector_operations()
    
    if test_passed:
        print("\nДемонстрация работы модуля:")
        print("-" * 40)
        
        # Примеры использования
        v1 = [1, 2, 3]
        v2 = [4, 5, 6]
        
        print(f"Вектор 1: {v1}")
        print(f"Вектор 2: {v2}")
        print()
        
        # Основные операции
        print(f"Сложение: {v1} + {v2} = {vector_addition(v1, v2)}")
        print(f"Вычитание: {v1} - {v2} = {vector_subtraction(v1, v2)}")
        print(f"Умножение на 2: {v1} * 2 = {vector_scalar_multiplication(v1, 2)}")
        print(f"Скалярное произведение: {v1}·{v2} = {vector_dot_product(v1, v2)}")
        print()
        
        # Анализ векторов
        print(f"Длина вектора 1: {vector_length(v1):.2f}")
        print(f"Минимальное и максимальное в векторе 1: {vector_min_max(v1)}")
        print(f"Среднее значение вектора 1: {vector_mean(v1):.2f}")
        print()
        
        # Нормализация
        v3 = [3, 4]
        normalized = normalize_vector(v3)
        print(f"Вектор: {v3}")
        print(f"Нормализованный: {normalized}")
        print(f"Длина нормализованного: {vector_length(normalized):.2f}")
    
    print("\n" + "=" * 60)
    print("Для использования модуля импортируйте его:")
    print("from vector_operations import *")
    print("или")
    print("import vector_operations as vo")
    print("=" * 60)
