def RemoveRows(A, K1, K2):
    """
    Удаляет из матрицы A размера M×N строки с номерами от K1 до K2 включительно.
    
    Параметры:
    A (list[list]): матрица M×N (список списков)
    K1 (int): номер первой строки для удаления (1-индексированный)
    K2 (int): номер последней строки для удаления (1-индексированный)
    
    Возвращает:
    list[list]: новая матрица с удаленными строками
    
    Примечания:
    - Если K1 > M, матрица не изменяется
    - Если K2 > M, удаляются строки с номерами от K1 до M
    - Индексация строк начинается с 1 (K1, K2 >= 1)
    - Предполагается, что 1 < K1 ≤ K2
    """
    
    # Проверка входных данных
    if not isinstance(A, list) or not all(isinstance(row, list) for row in A):
        raise TypeError("A должна быть матрицей (списком списков)")
    
    if not A:
        return []  # Пустая матрица
    
    # Проверка размеров матрицы
    M = len(A)  # Количество строк
    N = len(A[0]) if A else 0  # Количество столбцов
    
    # Проверка, что все строки имеют одинаковую длину
    if any(len(row) != N for row in A):
        raise ValueError("Все строки матрицы должны иметь одинаковую длину")
    
    # Проверка параметров K1 и K2
    if not isinstance(K1, int) or not isinstance(K2, int):
        raise TypeError("K1 и K2 должны быть целыми числами")
    
    if K1 <= 1:
        raise ValueError("K1 должно быть больше 1 (условие: 1 < K1 ≤ K2)")
    
    if K1 > K2:
        raise ValueError(f"K1 ({K1}) должно быть меньше или равно K2 ({K2})")
    
    # Проверка границ
    if K1 > M:
        # K1 больше количества строк - матрица не изменяется
        return [row[:] for row in A]  # Возвращаем копию
    
    # Корректируем K2, если он выходит за границы
    K2_corrected = min(K2, M)
    
    # Создаем новую матрицу без указанных строк
    # Помним, что K1 и K2 1-индексированные, а Python использует 0-индексацию
    new_matrix = []
    
    for i in range(M):
        # i - 0-индексированный номер текущей строки
        # Проверяем, нужно ли сохранять эту строку
        # Условие: строка должна быть вне диапазона [K1-1, K2_corrected-1]
        if i < (K1 - 1) or i > (K2_corrected - 1):
            new_matrix.append(A[i][:])  # Добавляем копию строки
    
    return new_matrix


def print_matrix(A, title="Матрица", indices_style=1):
    """
    Красиво выводит матрицу на экран.
    
    Параметры:
    A (list[list]): матрица для вывода
    title (str): заголовок матрицы
    indices_style (int): стиль индексации (0 для 0-based, 1 для 1-based)
    """
    if not A:
        print(f"{title}: []")
        return
    
    M = len(A)
    N = len(A[0]) if A else 0
    
    print(f"\n{title} ({M}×{N}):")
    
    # Определяем максимальную длину элемента для красивого форматирования
    max_len = 0
    for row in A:
        for element in row:
            max_len = max(max_len, len(str(element)))
    
    # Заголовок с номерами столбцов
    if indices_style == 1:
        col_header = "   " + " ".join(f"{j+1:>{max_len}}" for j in range(N))
    else:
        col_header = "   " + " ".join(f"{j:>{max_len}}" for j in range(N))
    print(col_header)
    
    # Разделитель
    print("  " + "-" * (N * (max_len + 1)))
    
    # Строки матрицы
    for i, row in enumerate(A):
        if indices_style == 1:
            row_num = f"{i+1:2}|"
        else:
            row_num = f"{i:2}|"
        
        elements = " ".join(f"{elem:>{max_len}}" for elem in row)
        print(f"{row_num} {elements}")


def create_matrix(M, N, fill_type='sequential'):
    """
    Создает тестовую матрицу размера M×N.
    
    Параметры:
    M (int): количество строк
    N (int): количество столбцов
    fill_type (str): тип заполнения:
        'sequential' - последовательные числа
        'random' - случайные числа
        'zeros' - нули
        'ones' - единицы
        'identity' - единичная матрица (если M==N)
    """
    import random
    
    matrix = []
    
    if fill_type == 'sequential':
        for i in range(M):
            row = []
            for j in range(N):
                row.append(i * N + j + 1)  # 1, 2, 3, ...
            matrix.append(row)
    
    elif fill_type == 'random':
        for i in range(M):
            row = []
            for j in range(N):
                row.append(random.randint(1, 100))
            matrix.append(row)
    
    elif fill_type == 'zeros':
        matrix = [[0] * N for _ in range(M)]
    
    elif fill_type == 'ones':
        matrix = [[1] * N for _ in range(M)]
    
    elif fill_type == 'identity' and M == N:
        matrix = [[1 if i == j else 0 for j in range(N)] for i in range(M)]
    else:
        # По умолчанию - последовательные числа
        return create_matrix(M, N, 'sequential')
    
    return matrix


def test_remove_rows():
    """Тестирование функции RemoveRows на различных случаях"""
    
    print("=" * 60)
    print("ТЕСТИРОВАНИЕ ФУНКЦИИ RemoveRows")
    print("=" * 60)
    
    # Создаем тестовую матрицу
    M, N = 6, 4
    A = create_matrix(M, N, 'sequential')
    
    print("Исходная матрица:")
    print_matrix(A, f"Матрица {M}×{N}")
    
    test_cases = [
        # (K1, K2, описание)
        (2, 4, "Удаление строк 2-4"),
        (3, 3, "Удаление одной строки (3)"),
        (4, 7, "K2 > M, удаление строк 4-6"),
        (7, 9, "K1 > M, матрица не изменяется"),
        (2, 6, "Удаление всех строк кроме первой"),
        (6, 6, "Удаление последней строки"),
    ]
    
    for K1, K2, description in test_cases:
        print(f"\n{description}: K1={K1}, K2={K2}")
        print("-" * 40)
        
        try:
            result = RemoveRows(A, K1, K2)
            remaining_rows = len(result)
            removed_rows = M - remaining_rows
            
            if removed_rows > 0:
                actual_K2 = min(K2, M)
                print(f"Удалено строк: {removed_rows} (с {K1} по {actual_K2})")
            else:
                print("Матрица не изменилась (K1 > M)")
            
            print(f"Результирующая матрица ({remaining_rows}×{N}):")
            print_matrix(result)
            
        except Exception as e:
            print(f"Ошибка: {type(e).__name__} - {e}")


def edge_cases_test():
    """Тестирование граничных случаев"""
    
    print("\n" + "=" * 60)
    print("ТЕСТИРОВАНИЕ ГРАНИЧНЫХ СЛУЧАЕВ")
    print("=" * 60)
    
    # Тест 1: Пустая матрица
    print("\n1. Пустая матрица:")
    A_empty = []
    result = RemoveRows(A_empty, 2, 4)
    print(f"   Исходная: {A_empty}")
    print(f"   Результат: {result}")
    
    # Тест 2: Матрица 1×N
    print("\n2. Матрица 1×3:")
    A_1x3 = [[1, 2, 3]]
    print_matrix(A_1x3, "Исходная")
    
    try:
        result = RemoveRows(A_1x3, 2, 3)
        print("   Удаление строк 2-3 (K1 > M) - матрица не изменилась:")
        print_matrix(result, "Результат")
    except Exception as e:
        print(f"   Ошибка: {e}")
    
    # Тест 3: Некорректные K1, K2
    print("\n3. Некорректные параметры K1, K2:")
    
    A_test = create_matrix(3, 3)
    
    invalid_cases = [
        (1, 2, "K1 = 1 (должно быть > 1)"),
        (3, 2, "K1 > K2"),
        (2.5, 3, "K1 не целое"),
        (2, "3", "K2 не целое"),
    ]
    
    for K1, K2, description in invalid_cases:
        print(f"   {description}: ", end="")
        try:
            RemoveRows(A_test, K1, K2)
            print("Ошибка не возникла (неожиданно!)")
        except Exception as e:
            print(f"{type(e).__name__}: {e}")
    
    # Тест 4: Матрица с разной длиной строк
    print("\n4. Матрица с разной длиной строк:")
    A_invalid = [[1, 2, 3], [4, 5], [6, 7, 8]]
    print(f"   Исходная: {A_invalid}")
    try:
        RemoveRows(A_invalid, 2, 2)
        print("   Ошибка не возникла (неожиданно!)")
    except ValueError as e:
        print(f"   ValueError: {e}")


def interactive_demo():
    """Интерактивная демонстрация"""
    
    print("\n" + "=" * 60)
    print("ИНТЕРАКТИВНАЯ ДЕМОНСТРАЦИЯ")
    print("=" * 60)
    
    while True:
        print("\n" + "-" * 40)
        print("Создание матрицы:")
        
        try:
            M = int(input("Введите количество строк M: "))
            N = int(input("Введите количество столбцов N: "))
            
            if M <= 0 or N <= 0:
                print("Размеры должны быть положительными!")
                continue
            
            print("\nВыберите тип заполнения:")
            print("1. Последовательные числа (1, 2, 3, ...)")
            print("2. Случайные числа (1-100)")
            print("3. Нули")
            print("4. Единицы")
            
            choice = input("Ваш выбор (1-4): ")
            
            fill_types = ['sequential', 'random', 'zeros', 'ones']
            fill_type = fill_types[int(choice) - 1] if choice.isdigit() and 1 <= int(choice) <= 4 else 'sequential'
            
            A = create_matrix(M, N, fill_type)
            print(f"\nСоздана матрица {M}×{N}:")
            print_matrix(A)
            
            print("\nУдаление строк:")
            K1 = int(input(f"Введите K1 (первая строка для удаления, 1 < K1 ≤ {M}): "))
            K2 = int(input(f"Введите K2 (последняя строка для удаления, K1 ≤ K2 ≤ {M}): "))
            
            if K1 <= 1:
                print("Ошибка: K1 должно быть больше 1!")
                continue
            
            if K1 > K2:
                print(f"Ошибка: K1 ({K1}) должно быть меньше или равно K2 ({K2})!")
                continue
            
            result = RemoveRows(A, K1, K2)
            
            print("\n" + "=" * 40)
            print("РЕЗУЛЬТАТ:")
            original_rows = len(A)
            result_rows = len(result)
            removed_rows = original_rows - result_rows
            
            if removed_rows > 0:
                actual_K2 = min(K2, original_rows)
                print(f"Удалено строк: {removed_rows} (с {K1} по {actual_K2})")
            else:
                print("Матрица не изменилась (K1 > M)")
            
            print(f"Исходный размер: {original_rows}×{N}")
            print(f"Финальный размер: {result_rows}×{N}")
            
            print("\nФинальная матрица:")
            print_matrix(result)
            
        except ValueError as e:
            print(f"Ошибка ввода: {e}")
        except Exception as e:
            print(f"Неожиданная ошибка: {type(e).__name__} - {e}")
        
        # Запрос на продолжение
        print("\n" + "-" * 40)
        cont = input("Продолжить? (y/n): ").lower()
        if cont != 'y':
            break


def performance_comparison():
    """Сравнение производительности с альтернативными подходами"""
    
    print("\n" + "=" * 60)
    print("СРАВНЕНИЕ ПРОИЗВОДИТЕЛЬНОСТИ")
    print("=" * 60)
    
    import time
    
    # Создаем большую матрицу для теста
    M, N = 1000, 100
    A = create_matrix(M, N, 'random')
    
    # Тестовые параметры
    K1, K2 = 200, 800
    
    print(f"Тестовая матрица: {M}×{N}")
    print(f"Удаление строк: с {K1} по {K2}")
    print()
    
    # Вариант 1: Наш алгоритм
    start = time.time()
    result1 = RemoveRows(A, K1, K2)
    time1 = time.time() - start
    
    print(f"1. Основной алгоритм:")
    print(f"   Время: {time1:.6f} сек")
    print(f"   Результат: {len(result1)}×{N}")
    
    # Вариант 2: Использование срезов
    def remove_rows_slice(A, K1, K2):
        if not A:
            return []
        
        M = len(A)
        if K1 > M:
            return [row[:] for row in A]
        
        K2_corrected = min(K2, M)
        # Используем срезы для более быстрого копирования
        return A[:K1-1] + A[K2_corrected:]
    
    start = time.time()
    result2 = remove_rows_slice(A, K1, K2)
    time2 = time.time() - start
    
    print(f"\n2. Алгоритм со срезами:")
    print(f"   Время: {time2:.6f} сек")
    print(f"   Результат: {len(result2)}×{N}")
    
    # Проверка эквивалентности результатов
    if result1 == result2:
        print(f"\n✓ Результаты идентичны")
        print(f"  Ускорение: {time1/time2:.2f}x")
    else:
        print("\n✗ Результаты различаются!")


# Дополнительные утилиты для работы с матрицами
def get_matrix_info(A):
    """Получить информацию о матрице"""
    if not A:
        return "Пустая матрица"
    
    M = len(A)
    N = len(A[0]) if A else 0
    
    # Проверка, является ли матрица квадратной
    is_square = M == N
    
    # Находим минимальное и максимальное значения
    flat_values = [elem for row in A for elem in row]
    min_val = min(flat_values) if flat_values else None
    max_val = max(flat_values) if flat_values else None
    sum_val = sum(flat_values) if flat_values else None
    
    info = f"Размер: {M}×{N}"
    if is_square:
        info += " (квадратная)"
    
    if min_val is not None:
        info += f"\nMin: {min_val}, Max: {max_val}, Sum: {sum_val}"
    
    return info


# Основная программа
if __name__ == "__main__":
    print("ФУНКЦИЯ RemoveRows - УДАЛЕНИЕ СТРОК ИЗ МАТРИЦЫ")
    print("=" * 60)
    
    # Запуск тестов
    test_remove_rows()
    
    # Граничные случаи
    edge_cases_test()
    
    # Сравнение производительности
    performance_comparison()
    
    # Интерактивная демонстрация
    interactive_demo()
    
    print("\n" + "=" * 60)
    print("ПРОГРАММА ЗАВЕРШЕНА")
    print("=" * 60)
