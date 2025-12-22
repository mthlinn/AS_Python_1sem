import os
import random
import numpy as np
from typing import List, Tuple, Union


def create_test_matrices_file(filename: str, k: int = 5, n: int = 3, min_val: int = -10, max_val: int = 10) -> None:
    """
    Создает тестовый файл с k матрицами размерности n×n.
    
    Параметры:
    filename (str): имя файла
    k (int): количество матриц
    n (int): размерность матриц (n×n)
    min_val (int): минимальное значение элемента
    max_val (int): максимальное значение элемента
    """
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            # Записываем размерность матриц
            f.write(f"{n}\n")
            
            for matrix_num in range(1, k + 1):
                # Создаем случайную матрицу
                matrix = []
                for i in range(n):
                    row = []
                    for j in range(n):
                        row.append(random.randint(min_val, max_val))
                    matrix.append(row)
                
                # Вычисляем сумму диагональных элементов
                diag_sum = sum(matrix[i][i] for i in range(n))
                
                # Записываем матрицу в файл
                f.write(f"Матрица {matrix_num} (сумма диагонали: {diag_sum}):\n")
                for i in range(n):
                    row_str = " ".join(f"{val:4}" for val in matrix[i])
                    f.write(row_str + "\n")
                f.write("\n")  # Разделитель между матрицами
        
        print(f"Создан файл '{filename}' с {k} матрицами {n}×{n}")
        print(f"Размер файла: {os.path.getsize(filename)} байт")
    
    except Exception as e:
        print(f"Ошибка при создании файла: {e}")


def parse_matrices_from_file(filename: str) -> Tuple[List[List[List[int]]], int, List[int]]:
    """
    Читает матрицы из файла.
    
    Параметры:
    filename (str): имя файла
    
    Возвращает:
    tuple: (matrices, n, diag_sums)
      matrices: список матриц
      n: размерность матриц
      diag_sums: список сумм диагоналей
    """
    matrices = []
    diag_sums = []
    n = None
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        i = 0
        matrix_num = 0
        
        while i < len(lines):
            line = lines[i].strip()
            
            # Пропускаем пустые строки
            if not line:
                i += 1
                continue
            
            # Если это первая строка файла, читаем размерность
            if n is None and line.isdigit():
                n = int(line)
                i += 1
                continue
            
            # Если строка начинается с "Матрица", начинаем читать новую матрицу
            if line.startswith("Матрица"):
                matrix_num += 1
                i += 1
                
                # Читаем n строк матрицы
                matrix = []
                for row_num in range(n):
                    if i >= len(lines):
                        break
                    
                    row_line = lines[i].strip()
                    # Разбираем строку на числа
                    try:
                        row = list(map(int, row_line.split()))
                        if len(row) == n:
                            matrix.append(row)
                        else:
                            print(f"Ошибка: строка {i+1} содержит {len(row)} чисел, ожидалось {n}")
                            return [], 0, []
                    except ValueError:
                        print(f"Ошибка в строке {i+1}: '{row_line}' не является числами")
                        return [], 0, []
                    
                    i += 1
                
                if len(matrix) == n:
                    matrices.append(matrix)
                    # Вычисляем сумму диагонали
                    diag_sum = sum(matrix[i][i] for i in range(n))
                    diag_sums.append(diag_sum)
                else:
                    print(f"Ошибка: матрица {matrix_num} имеет неправильный размер")
                    return [], 0, []
                
                # Пропускаем пустую строку после матрицы
                i += 1
            else:
                i += 1
        
        return matrices, n, diag_sums
    
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return [], 0, []


def calculate_diagonal_sum(matrix: List[List[int]]) -> int:
    """
    Вычисляет сумму диагональных элементов матрицы.
    
    Параметры:
    matrix (list): матрица n×n
    
    Возвращает:
    int: сумма диагональных элементов
    """
    n = len(matrix)
    return sum(matrix[i][i] for i in range(n))


def transpose_matrix(matrix: List[List[int]]) -> List[List[int]]:
    """
    Транспонирует матрицу.
    
    Параметры:
    matrix (list): исходная матрица n×n
    
    Возвращает:
    list: транспонированная матрица
    """
    n = len(matrix)
    transposed = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            transposed[i][j] = matrix[j][i]
    
    return transposed


def process_matrices_v1(input_filename: str, output_filename: str) -> Tuple[bool, dict]:
    """
    Обрабатывает матрицы из файла (версия 1).
    
    Параметры:
    input_filename (str): имя исходного файла
    output_filename (str): имя файла для матриц с нечетными суммами
    
    Возвращает:
    tuple: (success, stats)
    """
    stats = {
        'total_matrices': 0,
        'odd_sum_matrices': 0,
        'transposed_matrices': 0,
        'matrices_with_even_sum': 0
    }
    
    try:
        # Читаем матрицы из файла
        matrices, n, diag_sums = parse_matrices_from_file(input_filename)
        
        if n == 0:
            print("Ошибка: не удалось прочитать матрицы из файла")
            return False, stats
        
        stats['total_matrices'] = len(matrices)
        
        # Разделяем матрицы по четности суммы диагонали
        odd_sum_matrices = []
        even_sum_matrices = []
        odd_sum_indices = []
        
        for idx, (matrix, diag_sum) in enumerate(zip(matrices, diag_sums)):
            if diag_sum % 2 == 1:  # Нечетная сумма
                odd_sum_matrices.append(matrix)
                odd_sum_indices.append(idx)
                stats['odd_sum_matrices'] += 1
            else:
                even_sum_matrices.append(matrix)
                stats['matrices_with_even_sum'] += 1
        
        # Записываем матрицы с нечетными суммами в отдельный файл
        with open(output_filename, 'w', encoding='utf-8') as f_out:
            f_out.write(f"Матрицы с нечетной суммой диагональных элементов:\n")
            f_out.write(f"Всего матриц: {stats['odd_sum_matrices']}\n\n")
            
            for i, matrix in enumerate(odd_sum_matrices, 1):
                diag_sum = calculate_diagonal_sum(matrix)
                f_out.write(f"Матрица {i} (сумма диагонали: {diag_sum}):\n")
                for row in matrix:
                    row_str = " ".join(f"{val:4}" for val in row)
                    f_out.write(row_str + "\n")
                f_out.write("\n")
        
        # Транспонируем матрицы с нечетными суммами
        transposed_matrices = matrices.copy()
        
        for idx in odd_sum_indices:
            transposed_matrices[idx] = transpose_matrix(matrices[idx])
            stats['transposed_matrices'] += 1
        
        # Записываем обновленный исходный файл
        with open(input_filename, 'w', encoding='utf-8') as f_in:
            # Записываем размерность
            f_in.write(f"{n}\n\n")
            
            for i, matrix in enumerate(transposed_matrices, 1):
                diag_sum = calculate_diagonal_sum(matrix)
                f_in.write(f"Матрица {i} (сумма диагонали: {diag_sum}):\n")
                for row in matrix:
                    row_str = " ".join(f"{val:4}" for val in row)
                    f_in.write(row_str + "\n")
                f_in.write("\n")
        
        return True, stats
    
    except Exception as e:
        print(f"Ошибка при обработке файлов: {e}")
        return False, stats


def process_matrices_v2(input_filename: str, output_filename: str) -> Tuple[bool, dict]:
    """
    Обрабатывает матрицы из файла (версия 2, более эффективная).
    
    Параметры:
    input_filename (str): имя исходного файла
    output_filename (str): имя файла для матриц с нечетными суммами
    
    Возвращает:
    tuple: (success, stats)
    """
    stats = {
        'total_matrices': 0,
        'odd_sum_matrices': 0,
        'transposed_matrices': 0,
        'even_sum_matrices': 0
    }
    
    try:
        # Открываем файлы
        with open(input_filename, 'r', encoding='utf-8') as f_in:
            content = f_in.read()
        
        lines = content.split('\n')
        
        # Находим размерность n
        n = None
        for line in lines:
            if line.strip().isdigit():
                n = int(line.strip())
                break
        
        if n is None:
            print("Ошибка: не найдена размерность матриц в файле")
            return False, stats
        
        # Парсим матрицы
        matrices = []
        current_matrix = []
        in_matrix = False
        matrix_num = 0
        
        for line in lines:
            stripped = line.strip()
            
            if not stripped:
                continue
            
            if stripped.startswith("Матрица"):
                # Начало новой матрицы
                if current_matrix and len(current_matrix) == n:
                    matrices.append(current_matrix)
                    current_matrix = []
                
                matrix_num += 1
                in_matrix = True
                continue
            
            if in_matrix:
                # Читаем строку матрицы
                try:
                    row = list(map(int, stripped.split()))
                    if len(row) == n:
                        current_matrix.append(row)
                        
                        # Если собрали полную матрицу
                        if len(current_matrix) == n:
                            matrices.append(current_matrix)
                            current_matrix = []
                            in_matrix = False
                    else:
                        print(f"Ошибка: строка содержит {len(row)} чисел, ожидалось {n}")
                        return False, stats
                except ValueError:
                    # Если это не числа, пропускаем
                    continue
        
        # Добавляем последнюю матрицу, если есть
        if current_matrix and len(current_matrix) == n:
            matrices.append(current_matrix)
        
        stats['total_matrices'] = len(matrices)
        
        # Обработка матриц
        odd_sum_matrices = []
        updated_matrices = []
        
        for matrix in matrices:
            diag_sum = calculate_diagonal_sum(matrix)
            
            if diag_sum % 2 == 1:  # Нечетная сумма
                odd_sum_matrices.append(matrix)
                # Транспонируем для обновленного файла
                updated_matrices.append(transpose_matrix(matrix))
                stats['odd_sum_matrices'] += 1
                stats['transposed_matrices'] += 1
            else:
                updated_matrices.append(matrix)
                stats['even_sum_matrices'] += 1
        
        # Записываем матрицы с нечетными суммами
        with open(output_filename, 'w', encoding='utf-8') as f_out:
            f_out.write(f"Размерность матриц: {n}×{n}\n")
            f_out.write(f"Матрицы с нечетной суммой диагонали: {len(odd_sum_matrices)}\n\n")
            
            for i, matrix in enumerate(odd_sum_matrices, 1):
                diag_sum = calculate_diagonal_sum(matrix)
                f_out.write(f"Матрица {i} (сумма диагонали: {diag_sum}):\n")
                
                for row in matrix:
                    f_out.write("  " + "  ".join(f"{val:3}" for val in row) + "\n")
                
                f_out.write("\n")
        
        # Записываем обновленный исходный файл
        with open(input_filename, 'w', encoding='utf-8') as f_in:
            f_in.write(f"{n}\n\n")
            
            for i, matrix in enumerate(updated_matrices, 1):
                diag_sum = calculate_diagonal_sum(matrix)
                f_in.write(f"Матрица {i} (сумма диагонали: {diag_sum}):\n")
                
                for row in matrix:
                    f_in.write("  " + "  ".join(f"{val:3}" for val in row) + "\n")
                
                f_in.write("\n")
        
        return True, stats
    
    except Exception as e:
        print(f"Ошибка: {e}")
        return False, stats


def display_file_content(filename: str, title: str = "Содержимое файла", max_matrices: int = 5) -> None:
    """
    Выводит содержимое файла на экран.
    
    Параметры:
    filename (str): имя файла
    title (str): заголовок для вывода
    max_matrices (int): максимальное количество матриц для отображения
    """
    try:
        if not os.path.exists(filename):
            print(f"Файл '{filename}' не найден")
            return
        
        file_size = os.path.getsize(filename)
        print(f"\n{title}: '{filename}' (размер: {file_size} байт)")
        print("=" * 60)
        
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            print(content)
        
        print("=" * 60)
    
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")


def display_matrices_summary(matrices: List[List[List[int]]], diag_sums: List[int], title: str = "Матрицы") -> None:
    """
    Выводит сводную информацию о матрицах.
    
    Параметры:
    matrices (list): список матриц
    diag_sums (list): список сумм диагоналей
    title (str): заголовок
    """
    print(f"\n{title}:")
    print("-" * 50)
    print(f"Всего матриц: {len(matrices)}")
    
    if not matrices:
        return
    
    n = len(matrices[0])
    print(f"Размерность: {n}×{n}")
    print()
    
    for i, (matrix, diag_sum) in enumerate(zip(matrices, diag_sums), 1):
        parity = "нечетная" if diag_sum % 2 == 1 else "четная"
        print(f"Матрица {i}: сумма диагонали = {diag_sum} ({parity})")
        
        if i <= 3:  # Показываем только первые 3 матрицы полностью
            print("Матрица:")
            for row in matrix:
                print("  " + "  ".join(f"{val:3}" for val in row))
            print()


def compare_files(input_filename: str, output_filename: str) -> dict:
    """
    Сравнивает содержимое исходного и результирующего файлов.
    
    Параметры:
    input_filename (str): имя исходного файла
    output_filename (str): имя файла с нечетными матрицами
    
    Возвращает:
    dict: словарь со статистикой сравнения
    """
    comparison = {
        'input_exists': False,
        'output_exists': False,
        'input_matrices': 0,
        'output_matrices': 0,
        'all_odd_in_output': True,
        'input_updated': False
    }
    
    try:
        comparison['input_exists'] = os.path.exists(input_filename)
        comparison['output_exists'] = os.path.exists(output_filename)
        
        if comparison['input_exists']:
            matrices, n, diag_sums = parse_matrices_from_file(input_filename)
            comparison['input_matrices'] = len(matrices)
            
            # Проверяем, есть ли матрицы с нечетными суммами
            odd_sum_indices = [i for i, s in enumerate(diag_sums) if s % 2 == 1]
            comparison['input_odd_matrices'] = len(odd_sum_indices)
        
        if comparison['output_exists']:
            output_matrices, n_out, output_diag_sums = parse_matrices_from_file(output_filename)
            comparison['output_matrices'] = len(output_matrices)
            
            # Проверяем, что все матрицы в output имеют нечетные суммы
            all_odd = all(s % 2 == 1 for s in output_diag_sums)
            comparison['all_odd_in_output'] = all_odd
        
        # Если оба файла существуют
        if comparison['input_exists'] and comparison['output_exists']:
            # Проверяем, что количество матриц в output равно количеству нечетных в input
            comparison['counts_match'] = (comparison['output_matrices'] == comparison['input_odd_matrices'])
            
            # Проверяем, что матрицы в input были транспонированы (если были нечетными)
            if 'input_odd_matrices' in comparison and comparison['input_odd_matrices'] > 0:
                # Для проверки нужно проанализировать сами матрицы
                pass
        
        return comparison
    
    except Exception as e:
        print(f"Ошибка при сравнении файлов: {e}")
        return comparison


def validate_matrix(matrix: List[List[int]]) -> bool:
    """
    Проверяет, является ли матрица квадратной.
    
    Параметры:
    matrix (list): матрица для проверки
    
    Возвращает:
    bool: True, если матрица квадратная
    """
    if not matrix:
        return False
    
    n = len(matrix)
    
    # Проверяем, что все строки имеют длину n
    for row in matrix:
        if len(row) != n:
            return False
    
    return True


def matrix_to_string(matrix: List[List[int]], matrix_num: int = None) -> str:
    """
    Преобразует матрицу в строку для вывода.
    
    Параметры:
    matrix (list): матрица
    matrix_num (int): номер матрицы
    
    Возвращает:
    str: строковое представление матрицы
    """
    n = len(matrix)
    result = ""
    
    if matrix_num is not None:
        diag_sum = calculate_diagonal_sum(matrix)
        result += f"Матрица {matrix_num} (сумма диагонали: {diag_sum}):\n"
    
    for row in matrix:
        result += "  " + "  ".join(f"{val:4}" for val in row) + "\n"
    
    return result


def interactive_mode():
    """
    Интерактивный режим работы программы.
    """
    print("=" * 70)
    print("ОБРАБОТКА МАТРИЦ ИЗ ФАЙЛА")
    print("=" * 70)
    
    while True:
        print("\nМеню:")
        print("1. Создать тестовый файл с матрицами")
        print("2. Обработать матрицы (версия 1)")
        print("3. Обработать матрицы (версия 2)")
        print("4. Показать содержимое файлов")
        print("5. Сравнить файлы")
        print("6. Протестировать отдельные функции")
        print("0. Выход")
        
        choice = input("\nВыберите действие (0-6): ").strip()
        
        if choice == '0':
            print("Выход из программы...")
            break
        
        elif choice == '1':
            # Создание тестового файла
            filename = input("Введите имя файла (по умолчанию: matrices.txt): ").strip()
            if not filename:
                filename = "matrices.txt"
            
            try:
                k = int(input("Количество матриц (по умолчанию: 5): ") or "5")
                n = int(input("Размерность матриц n (по умолчанию: 3): ") or "3")
                min_val = int(input("Минимальное значение (по умолчанию: -10): ") or "-10")
                max_val = int(input("Максимальное значение (по умолчанию: 10): ") or "10")
                
                create_test_matrices_file(filename, k, n, min_val, max_val)
                
            except ValueError:
                print("Ошибка: введите корректные числа")
        
        elif choice in ['2', '3']:
            # Обработка матриц
            input_file = input("Введите имя исходного файла (по умолчанию: matrices.txt): ").strip()
            if not input_file:
                input_file = "matrices.txt"
            
            output_file = input("Введите имя файла для нечетных матриц (по умолчанию: odd_matrices.txt): ").strip()
            if not output_file:
                output_file = "odd_matrices.txt"
            
            print("\n" + "=" * 50)
            
            if choice == '2':
                success, stats = process_matrices_v1(input_file, output_file)
            else:
                success, stats = process_matrices_v2(input_file, output_file)
            
            if success:
                print("✓ Операция выполнена успешно!")
                print(f"  Всего матриц: {stats['total_matrices']}")
                print(f"  Матриц с нечетной суммой: {stats['odd_sum_matrices']}")
                print(f"  Матриц с четной суммой: {stats.get('even_sum_matrices', stats.get('matrices_with_even_sum', 0))}")
                print(f"  Транспонировано матриц: {stats['transposed_matrices']}")
                
                # Показываем содержимое файлов
                show_files = input("\nПоказать содержимое файлов? (y/n): ").strip().lower()
                if show_files == 'y':
                    display_file_content(input_file, "Исходный файл (обновленный)")
                    display_file_content(output_file, "Файл с нечетными матрицами")
        
        elif choice == '4':
            # Показать содержимое файлов
            input_file = input("Введите имя исходного файла (по умолчанию: matrices.txt): ").strip()
            if not input_file:
                input_file = "matrices.txt"
            
            output_file = input("Введите имя файла с нечетными матрицами (по умолчанию: odd_matrices.txt): ").strip()
            if not output_file:
                output_file = "odd_matrices.txt"
            
            display_file_content(input_file, "Исходный файл")
            display_file_content(output_file, "Файл с нечетными матрицами")
        
        elif choice == '5':
            # Сравнить файлы
            input_file = input("Введите имя исходного файла (по умолчанию: matrices.txt): ").strip()
            if not input_file:
                input_file = "matrices.txt"
            
            output_file = input("Введите имя файла с нечетными матрицами (по умолчанию: odd_matrices.txt): ").strip()
            if not output_file:
                output_file = "odd_matrices.txt"
            
            comparison = compare_files(input_file, output_file)
            
            print("\nСравнение файлов:")
            print(f"  Исходный файл существует: {'Да' if comparison['input_exists'] else 'Нет'}")
            print(f"  Файл с нечетными матрицами существует: {'Да' if comparison['output_exists'] else 'Нет'}")
            
            if comparison['input_exists']:
                print(f"  Матриц в исходном файле: {comparison['input_matrices']}")
                print(f"  Матриц с нечетной суммой в исходном: {comparison.get('input_odd_matrices', 'N/A')}")
            
            if comparison['output_exists']:
                print(f"  Матриц в файле с нечетными: {comparison['output_matrices']}")
                print(f"  Все матрицы в output нечетные: {'Да' if comparison['all_odd_in_output'] else 'Нет'}")
            
            if comparison['input_exists'] and comparison['output_exists']:
                if comparison.get('counts_match', False):
                    print("  ✓ Количества совпадают")
                else:
                    print("  ⚠ Количества не совпадают")
        
        elif choice == '6':
            # Тестирование отдельных функций
            print("\nТестирование функций:")
            
            # Тестовая матрица 3x3
            test_matrix = [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]
            ]
            
            print("1. Тестовая матрица 3x3:")
            for row in test_matrix:
                print("  " + "  ".join(f"{val:2}" for val in row))
            
            diag_sum = calculate_diagonal_sum(test_matrix)
            print(f"   Сумма диагонали: {diag_sum} ({'нечетная' if diag_sum % 2 == 1 else 'четная'})")
            
            transposed = transpose_matrix(test_matrix)
            print("\n2. Транспонированная матрица:")
            for row in transposed:
                print("  " + "  ".join(f"{val:2}" for val in row))
            
            is_square = validate_matrix(test_matrix)
            print(f"\n3. Матрица квадратная: {'Да' if is_square else 'Нет'}")
            
            # Создаем неквадратную матрицу для теста
            non_square = [
                [1, 2, 3],
                [4, 5, 6]
            ]
            is_square2 = validate_matrix(non_square)
            print(f"4. Неквадратная матрица (2x3): {'Да' if is_square2 else 'Нет'}")
        
        else:
            print("Неверный выбор. Попробуйте снова.")


def demonstrate_example():
    """
    Демонстрационный пример работы программы.
    """
    print("\n" + "=" * 70)
    print("ДЕМОНСТРАЦИОННЫЙ ПРИМЕР")
    print("=" * 70)
    
    # Создаем тестовые файлы
    input_file = "demo_matrices.txt"
    output_file = "demo_odd_matrices.txt"
    
    # Создаем тестовые данные
    test_matrices = [
        # Матрица 1: сумма диагонали = 1+5+9 = 15 (нечетная)
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ],
        # Матрица 2: сумма диагонали = 2+5+8 = 15 (нечетная)
        [
            [2, 0, 0],
            [0, 5, 0],
            [0, 0, 8]
        ],
        # Матрица 3: сумма диагонали = 0+0+0 = 0 (четная)
        [
            [0, 1, 2],
            [3, 0, 4],
            [5, 6, 0]
        ],
        # Матрица 4: сумма диагонали = 4+5+6 = 15 (нечетная)
        [
            [4, 0, 0],
            [0, 5, 0],
            [0, 0, 6]
        ],
        # Матрица 5: сумма диагонали = 2+2+2 = 6 (четная)
        [
            [2, 1, 0],
            [1, 2, 1],
            [0, 1, 2]
        ]
    ]
    
    print("Тестовые матрицы 3x3:")
    for i, matrix in enumerate(test_matrices, 1):
        diag_sum = calculate_diagonal_sum(matrix)
        parity = "нечетная" if diag_sum % 2 == 1 else "четная"
        print(f"Матрица {i}: сумма диагонали = {diag_sum} ({parity})")
    
    # Записываем тестовые данные в файл
    n = 3
    with open(input_file, 'w', encoding='utf-8') as f:
        f.write(f"{n}\n\n")
        
        for i, matrix in enumerate(test_matrices, 1):
            diag_sum = calculate_diagonal_sum(matrix)
            f.write(f"Матрица {i} (сумма диагонали: {diag_sum}):\n")
            
            for row in matrix:
                f.write("  " + "  ".join(f"{val:3}" for val in row) + "\n")
            
            f.write("\n")
    
    print(f"\nСоздан файл '{input_file}'")
    
    # Обрабатываем матрицы
    print("\nОбработка матриц...")
    success, stats = process_matrices_v1(input_file, output_file)
    
    if success:
        print("✓ Обработка завершена успешно!")
        print(f"  Всего матриц: {stats['total_matrices']}")
        print(f"  Матриц с нечетной суммой: {stats['odd_sum_matrices']}")
        print(f"  Транспонировано матриц: {stats['transposed_matrices']}")
        
        # Показываем содержимое файлов
        print("\n" + "=" * 50)
        print("Содержимое исходного файла (обновленного):")
        display_file_content(input_file, "", max_matrices=10)
        
        print("\n" + "=" * 50)
        print("Содержимое файла с нечетными матрицами:")
        display_file_content(output_file, "", max_matrices=10)
        
        # Проверяем корректность
        print("\n" + "=" * 50)
        print("Проверка корректности:")
        
        # Читаем обновленный файл
        updated_matrices, n_upd, updated_sums = parse_matrices_from_file(input_file)
        
        # Проверяем, что матрицы с нечетными суммами транспонированы
        original_odd_indices = [0, 1, 3]  # Индексы матриц с нечетными суммами в исходных данных
        
        for idx in original_odd_indices:
            if idx < len(updated_matrices):
                # Проверяем, транспонирована ли матрица
                original = test_matrices[idx]
                updated = updated_matrices[idx]
                
                # Проверяем транспонирование
                is_transposed = True
                for i in range(n):
                    for j in range(n):
                        if updated[i][j] != original[j][i]:
                            is_transposed = False
                            break
                    if not is_transposed:
                        break
                
                if is_transposed:
                    print(f"✓ Матрица {idx+1} корректно транспонирована")
                else:
                    print(f"⚠ Матрица {idx+1} не была транспонирована")
        
        # Проверяем файл с нечетными матрицами
        odd_matrices, n_odd, odd_sums = parse_matrices_from_file(output_file)
        all_odd = all(s % 2 == 1 for s in odd_sums)
        
        if all_odd:
            print(f"✓ Все матрицы в файле с нечетными имеют нечетные суммы ({len(odd_matrices)} матриц)")
        else:
            print(f"⚠ В файле с нечетными есть матрицы с четными суммами")
    
    # Удаляем временные файлы
    if os.path.exists(input_file):
        os.remove(input_file)
        print(f"\nУдален временный файл: {input_file}")
    
    if os.path.exists(output_file):
        os.remove(output_file)
        print(f"Удален временный файл: {output_file}")


# Основная программа
if __name__ == "__main__":
    print("ОБРАБОТКА МАТРИЦ: ВЫЧИСЛЕНИЕ СУММ ДИАГОНАЛЕЙ И ТРАНСПОНИРОВАНИЕ")
    print("=" * 70)
    
    # Демонстрационный пример
    demonstrate_example()
    
    # Интерактивный режим
    interactive_mode()
    
    print("\n" + "=" * 70)
    print("Программа завершена")
    print("=" * 70)
