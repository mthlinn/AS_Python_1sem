import os
import random
import struct
from typing import List, Union, BinaryIO


def create_test_file_f(filename: str, num_count: int = 20, min_val: int = -100, max_val: int = 100) -> None:
    """
    Создает тестовый файл f с целыми числами.
    
    Параметры:
    filename (str): имя файла
    num_count (int): количество чисел для записи
    min_val (int): минимальное значение
    max_val (int): максимальное значение
    """
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            numbers = []
            for i in range(num_count):
                num = random.randint(min_val, max_val)
                numbers.append(num)
                f.write(f"{num}")
                if i < num_count - 1:
                    f.write(" ")
            
            # Подсчет четных чисел для проверки
            even_count = sum(1 for num in numbers if num % 2 == 0)
            print(f"Создан файл '{filename}' с {num_count} числами")
            print(f"Из них четных: {even_count}")
            print(f"Числа: {numbers}")
    
    except Exception as e:
        print(f"Ошибка при создании файла: {e}")


def create_test_file_binary(filename: str, num_count: int = 20) -> None:
    """
    Создает тестовый бинарный файл f с целыми числами.
    
    Параметры:
    filename (str): имя файла
    num_count (int): количество чисел для записи
    """
    try:
        with open(filename, 'wb') as f:
            numbers = []
            for _ in range(num_count):
                num = random.randint(-100, 100)
                numbers.append(num)
                # Записываем 4-байтовое целое число
                f.write(struct.pack('i', num))
            
            even_count = sum(1 for num in numbers if num % 2 == 0)
            print(f"Создан бинарный файл '{filename}' с {num_count} числами")
            print(f"Из них четных: {even_count}")
    
    except Exception as e:
        print(f"Ошибка при создании бинарного файла: {e}")


def filter_even_numbers_v1(f_filename: str, g_filename: str) -> tuple:
    """
    Версия 1: Чтение файла как текстового, разделение по пробелам.
    
    Параметры:
    f_filename (str): имя исходного файла
    g_filename (str): имя результирующего файла
    
    Возвращает:
    tuple: (success, even_numbers_count, total_numbers)
    """
    try:
        # Проверка существования файла f
        if not os.path.exists(f_filename):
            print(f"Ошибка: файл '{f_filename}' не найден")
            return (False, 0, 0)
        
        # Чтение файла f
        with open(f_filename, 'r', encoding='utf-8') as f:
            content = f.read().strip()
            
            if not content:
                print(f"Файл '{f_filename}' пуст")
                # Создаем пустой файл g
                with open(g_filename, 'w', encoding='utf-8') as g:
                    pass
                return (True, 0, 0)
            
            # Разделяем строку на числа
            try:
                numbers = list(map(int, content.split()))
            except ValueError as e:
                print(f"Ошибка: файл содержит нечисловые данные: {e}")
                return (False, 0, 0)
        
        # Фильтрация четных чисел
        even_numbers = [num for num in numbers if num % 2 == 0]
        total_numbers = len(numbers)
        even_count = len(even_numbers)
        
        # Запись в файл g
        with open(g_filename, 'w', encoding='utf-8') as g:
            if even_numbers:
                g.write(" ".join(map(str, even_numbers)))
            else:
                # Создаем пустой файл
                pass
        
        return (True, even_count, total_numbers)
    
    except PermissionError:
        print(f"Ошибка: недостаточно прав для работы с файлами")
        return (False, 0, 0)
    except Exception as e:
        print(f"Неизвестная ошибка: {e}")
        return (False, 0, 0)


def filter_even_numbers_v2(f_filename: str, g_filename: str) -> tuple:
    """
    Версия 2: Чтение файла построчно с обработкой нескольких чисел в строке.
    
    Параметры:
    f_filename (str): имя исходного файла
    g_filename (str): имя результирующего файла
    
    Возвращает:
    tuple: (success, even_numbers_count, total_numbers)
    """
    try:
        if not os.path.exists(f_filename):
            print(f"Ошибка: файл '{f_filename}' не найден")
            return (False, 0, 0)
        
        all_numbers = []
        
        with open(f_filename, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue  # Пропускаем пустые строки
                
                try:
                    # Разбираем числа в строке
                    numbers_in_line = list(map(int, line.split()))
                    all_numbers.extend(numbers_in_line)
                except ValueError as e:
                    print(f"Ошибка в строке {line_num}: {e}")
                    return (False, 0, 0)
        
        if not all_numbers:
            # Создаем пустой файл g
            with open(g_filename, 'w', encoding='utf-8') as g:
                pass
            return (True, 0, 0)
        
        # Фильтрация четных чисел
        even_numbers = [num for num in all_numbers if num % 2 == 0]
        total_numbers = len(all_numbers)
        even_count = len(even_numbers)
        
        # Запись в файл g
        with open(g_filename, 'w', encoding='utf-8') as g:
            for i, num in enumerate(even_numbers):
                g.write(str(num))
                if i < len(even_numbers) - 1:
                    g.write(" ")
        
        return (True, even_count, total_numbers)
    
    except Exception as e:
        print(f"Ошибка: {e}")
        return (False, 0, 0)


def filter_even_numbers_v3(f_filename: str, g_filename: str, delimiter: str = None) -> tuple:
    """
    Версия 3: Расширенная версия с поддержкой различных разделителей.
    
    Параметры:
    f_filename (str): имя исходного файла
    g_filename (str): имя результирующего файла
    delimiter (str): разделитель чисел (если None, пробелы и переносы строк)
    
    Возвращает:
    tuple: (success, even_numbers_count, total_numbers, processing_stats)
    """
    import re
    
    try:
        if not os.path.exists(f_filename):
            print(f"Ошибка: файл '{f_filename}' не найден")
            return (False, 0, 0, {})
        
        stats = {
            'lines_read': 0,
            'numbers_found': 0,
            'even_numbers': 0,
            'odd_numbers': 0,
            'errors': 0
        }
        
        all_numbers = []
        
        with open(f_filename, 'r', encoding='utf-8') as f:
            for line in f:
                stats['lines_read'] += 1
                line = line.strip()
                
                if not line:
                    continue
                
                if delimiter:
                    # Используем заданный разделитель
                    parts = line.split(delimiter)
                else:
                    # Используем регулярное выражение для поиска чисел
                    # Ищем целые числа (возможно с отрицательным знаком)
                    parts = re.findall(r'-?\d+', line)
                
                for part in parts:
                    try:
                        num = int(part.strip())
                        all_numbers.append(num)
                        stats['numbers_found'] += 1
                        
                        if num % 2 == 0:
                            stats['even_numbers'] += 1
                        else:
                            stats['odd_numbers'] += 1
                    except ValueError:
                        stats['errors'] += 1
                        # Пропускаем некорректные данные
        
        if not all_numbers:
            # Создаем пустой файл g
            with open(g_filename, 'w', encoding='utf-8') as g:
                pass
            return (True, 0, 0, stats)
        
        # Фильтрация четных чисел
        even_numbers = [num for num in all_numbers if num % 2 == 0]
        
        # Запись в файл g
        with open(g_filename, 'w', encoding='utf-8') as g:
            if even_numbers:
                # Записываем с разделителем - запятой и пробелом для удобства чтения
                g.write(", ".join(map(str, even_numbers)))
        
        return (True, len(even_numbers), len(all_numbers), stats)
    
    except Exception as e:
        print(f"Ошибка: {e}")
        return (False, 0, 0, {})


def filter_even_numbers_binary(f_filename: str, g_filename: str) -> tuple:
    """
    Обработка бинарного файла с целыми числами.
    
    Параметры:
    f_filename (str): имя исходного бинарного файла
    g_filename (str): имя результирующего файла
    
    Возвращает:
    tuple: (success, even_numbers_count, total_numbers)
    """
    try:
        if not os.path.exists(f_filename):
            print(f"Ошибка: файл '{f_filename}' не найден")
            return (False, 0, 0)
        
        # Получаем размер файла
        file_size = os.path.getsize(f_filename)
        int_size = struct.calcsize('i')  # Размер одного целого числа в байтах
        
        if file_size % int_size != 0:
            print(f"Предупреждение: размер файла не кратен размеру целого числа")
        
        total_numbers = file_size // int_size
        even_numbers = []
        
        # Чтение бинарного файла
        with open(f_filename, 'rb') as f:
            # Читаем файл блоками
            while True:
                chunk = f.read(int_size)
                if not chunk:
                    break
                
                try:
                    num = struct.unpack('i', chunk)[0]
                    if num % 2 == 0:
                        even_numbers.append(num)
                except struct.error:
                    print(f"Ошибка при чтении бинарных данных")
                    continue
        
        # Запись результата в текстовый файл
        with open(g_filename, 'w', encoding='utf-8') as g:
            if even_numbers:
                g.write(" ".join(map(str, even_numbers)))
        
        return (True, len(even_numbers), total_numbers)
    
    except Exception as e:
        print(f"Ошибка при работе с бинарным файлом: {e}")
        return (False, 0, 0)


def read_and_display_file(filename: str, max_display: int = 20, description: str = "Содержимое файла") -> None:
    """
    Читает и отображает содержимое файла.
    
    Параметры:
    filename (str): имя файла
    max_display (int): максимальное количество чисел для отображения
    description (str): описание файла
    """
    try:
        if not os.path.exists(filename):
            print(f"Файл '{filename}' не найден")
            return
        
        file_size = os.path.getsize(filename)
        print(f"\n{description}: '{filename}' (размер: {file_size} байт)")
        print("-" * 50)
        
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            
            if not content.strip():
                print("(файл пуст)")
                return
            
            # Разбираем числа для отображения
            try:
                numbers = list(map(int, content.split()))
                
                if len(numbers) <= max_display:
                    print(f"Числа: {numbers}")
                    print(f"Количество чисел: {len(numbers)}")
                else:
                    print(f"Первые {max_display} чисел: {numbers[:max_display]}")
                    print(f"... и еще {len(numbers) - max_display} чисел")
                    print(f"Всего чисел: {len(numbers)}")
                
                # Дополнительная статистика
                if numbers:
                    print(f"Минимум: {min(numbers)}")
                    print(f"Максимум: {max(numbers)}")
                    print(f"Сумма: {sum(numbers)}")
                    
            except ValueError:
                # Если не удалось разобрать как числа, показываем как есть
                print("Содержимое (не только числа):")
                if len(content) > 100:
                    print(content[:100] + "...")
                else:
                    print(content)
        
        print("-" * 50)
    
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")


def compare_files_statistics(f_filename: str, g_filename: str) -> dict:
    """
    Сравнивает статистику двух файлов.
    
    Параметры:
    f_filename (str): имя исходного файла
    g_filename (str): имя результирующего файла
    
    Возвращает:
    dict: словарь со статистикой
    """
    stats = {
        'f_exists': False,
        'g_exists': False,
        'f_numbers': 0,
        'g_numbers': 0,
        'f_evens': 0,
        'all_even_in_g': True,
        'file_sizes': {}
    }
    
    try:
        # Проверка существования файлов
        stats['f_exists'] = os.path.exists(f_filename)
        stats['g_exists'] = os.path.exists(g_filename)
        
        if stats['f_exists']:
            stats['file_sizes']['f'] = os.path.getsize(f_filename)
            
            # Чтение файла f
            with open(f_filename, 'r', encoding='utf-8') as f:
                content = f.read()
                try:
                    numbers_f = list(map(int, content.split()))
                    stats['f_numbers'] = len(numbers_f)
                    stats['f_evens'] = sum(1 for num in numbers_f if num % 2 == 0)
                except:
                    stats['f_numbers'] = 0
                    stats['f_evens'] = 0
        
        if stats['g_exists']:
            stats['file_sizes']['g'] = os.path.getsize(g_filename)
            
            # Чтение файла g
            with open(g_filename, 'r', encoding='utf-8') as g:
                content = g.read()
                try:
                    numbers_g = list(map(int, content.split()))
                    stats['g_numbers'] = len(numbers_g)
                except:
                    stats['g_numbers'] = 0
        
        # Проверка корректности
        if stats['f_exists'] and stats['g_exists']:
            stats['all_even_in_g'] = (stats['g_numbers'] == stats['f_evens'])
        
        return stats
    
    except Exception as e:
        print(f"Ошибка при сравнении файлов: {e}")
        return stats


def interactive_mode():
    """
    Интерактивный режим работы программы.
    """
    print("=" * 60)
    print("ФИЛЬТРАЦИЯ ЧЁТНЫХ ЧИСЕЛ ИЗ ФАЙЛА")
    print("=" * 60)
    
    while True:
        print("\nМеню:")
        print("1. Создать тестовый файл f")
        print("2. Создать бинарный тестовый файл f")
        print("3. Отфильтровать чётные числа (версия 1)")
        print("4. Отфильтровать чётные числа (версия 2)")
        print("5. Отфильтровать чётные числа (версия 3 с разделителем)")
        print("6. Обработать бинарный файл")
        print("7. Показать содержимое файлов")
        print("8. Сравнить статистику файлов")
        print("9. Обработать несколько файлов")
        print("0. Выход")
        
        choice = input("\nВыберите действие (0-9): ").strip()
        
        if choice == '0':
            print("Выход из программы...")
            break
        
        elif choice == '1':
            # Создание тестового файла
            filename = input("Введите имя файла (по умолчанию: f.txt): ").strip()
            if not filename:
                filename = "f.txt"
            
            try:
                count = int(input("Сколько чисел сгенерировать? (по умолчанию: 20): ") or "20")
                min_val = int(input("Минимальное значение? (по умолчанию: -100): ") or "-100")
                max_val = int(input("Максимальное значение? (по умолчанию: 100): ") or "100")
                
                create_test_file_f(filename, count, min_val, max_val)
                
            except ValueError:
                print("Ошибка: введите корректные числа")
        
        elif choice == '2':
            # Создание бинарного тестового файла
            filename = input("Введите имя файла (по умолчанию: f.bin): ").strip()
            if not filename:
                filename = "f.bin"
            
            try:
                count = int(input("Сколько чисел сгенерировать? (по умолчанию: 20): ") or "20")
                create_test_file_binary(filename, count)
                
            except ValueError:
                print("Ошибка: введите корректное число")
        
        elif choice in ['3', '4', '5']:
            # Фильтрация чётных чисел
            f_file = input("Введите имя исходного файла f (по умолчанию: f.txt): ").strip()
            if not f_file:
                f_file = "f.txt"
            
            g_file = input("Введите имя результирующего файла g (по умолчанию: g.txt): ").strip()
            if not g_file:
                g_file = "g.txt"
            
            if choice == '3':
                success, even_count, total = filter_even_numbers_v1(f_file, g_file)
                if success:
                    print(f"\nУспешно обработано!")
                    print(f"Всего чисел в f: {total}")
                    print(f"Чётных чисел: {even_count}")
                    print(f"Записано в файл g: {even_count}")
            
            elif choice == '4':
                success, even_count, total = filter_even_numbers_v2(f_file, g_file)
                if success:
                    print(f"\nУспешно обработано!")
                    print(f"Всего чисел в f: {total}")
                    print(f"Чётных чисел: {even_count}")
                    print(f"Записано в файл g: {even_count}")
            
            elif choice == '5':
                delimiter = input("Введите разделитель (оставьте пустым для пробелов): ").strip()
                if delimiter == '':
                    delimiter = None
                
                success, even_count, total, stats = filter_even_numbers_v3(f_file, g_file, delimiter)
                if success:
                    print(f"\nУспешно обработано!")
                    print(f"Всего чисел в f: {total}")
                    print(f"Чётных чисел: {even_count}")
                    print(f"Статистика: строк прочитано: {stats.get('lines_read', 0)}, "
                          f"ошибок: {stats.get('errors', 0)}")
        
        elif choice == '6':
            # Обработка бинарного файла
            f_file = input("Введите имя исходного бинарного файла f (по умолчанию: f.bin): ").strip()
            if not f_file:
                f_file = "f.bin"
            
            g_file = input("Введите имя результирующего файла g (по умолчанию: g.txt): ").strip()
            if not g_file:
                g_file = "g.txt"
            
            success, even_count, total = filter_even_numbers_binary(f_file, g_file)
            if success:
                print(f"\nУспешно обработано!")
                print(f"Всего чисел в f: {total}")
                print(f"Чётных чисел: {even_count}")
                print(f"Записано в файл g: {even_count}")
        
        elif choice == '7':
            # Показать содержимое файлов
            f_file = input("Введите имя файла f для просмотра (по умолчанию: f.txt): ").strip()
            if not f_file:
                f_file = "f.txt"
            
            g_file = input("Введите имя файла g для просмотра (по умолчанию: g.txt): ").strip()
            if not g_file:
                g_file = "g.txt"
            
            read_and_display_file(f_file, description="Исходный файл f")
            read_and_display_file(g_file, description="Результирующий файл g")
        
        elif choice == '8':
            # Сравнить статистику файлов
            f_file = input("Введите имя файла f (по умолчанию: f.txt): ").strip()
            if not f_file:
                f_file = "f.txt"
            
            g_file = input("Введите имя файла g (по умолчанию: g.txt): ").strip()
            if not g_file:
                g_file = "g.txt"
            
            stats = compare_files_statistics(f_file, g_file)
            
            print("\nСтатистика сравнения файлов:")
            print(f"  Файл f существует: {'Да' if stats['f_exists'] else 'Нет'}")
            print(f"  Файл g существует: {'Да' if stats['g_exists'] else 'Нет'}")
            
            if stats['f_exists']:
                print(f"  Числа в f: {stats['f_numbers']}")
                print(f"  Чётных в f: {stats['f_evens']}")
                print(f"  Размер f: {stats['file_sizes'].get('f', 0)} байт")
            
            if stats['g_exists']:
                print(f"  Числа в g: {stats['g_numbers']}")
                print(f"  Размер g: {stats['file_sizes'].get('g', 0)} байт")
            
            if stats['f_exists'] and stats['g_exists']:
                if stats['all_even_in_g']:
                    print(f"  ✓ Все чётные числа из f присутствуют в g")
                else:
                    print(f"  ⚠ Расхождение: в g должно быть {stats['f_evens']} чисел, а есть {stats['g_numbers']}")
        
        elif choice == '9':
            # Обработка нескольких файлов
            print("\nПакетная обработка файлов:")
            files_input = input("Введите имена файлов f через запятую (например: f1.txt,f2.txt): ").strip()
            if not files_input:
                print("Ошибка: не указаны файлы")
                continue
            
            f_files = [f.strip() for f in files_input.split(',')]
            results = []
            
            for f_file in f_files:
                # Создаем имя для g-файла
                base_name = os.path.splitext(f_file)[0]
                g_file = f"{base_name}_even.txt"
                
                print(f"\nОбработка {f_file} -> {g_file}")
                success, even_count, total = filter_even_numbers_v1(f_file, g_file)
                
                results.append({
                    'f_file': f_file,
                    'g_file': g_file,
                    'success': success,
                    'total': total,
                    'even': even_count
                })
                
                if success:
                    print(f"  Успешно: {even_count}/{total} чётных чисел")
                else:
                    print(f"  Ошибка при обработке")
            
            # Вывод сводки
            print("\n" + "=" * 50)
            print("Сводка пакетной обработки:")
            for res in results:
                status = "✓" if res['success'] else "✗"
                print(f"{status} {res['f_file']} -> {res['g_file']}: "
                      f"{res['even']}/{res['total']} чётных")
        
        else:
            print("Неверный выбор. Попробуйте снова.")


def demonstrate_example():
    """
    Демонстрационный пример работы программы.
    """
    print("\n" + "=" * 60)
    print("ДЕМОНСТРАЦИОННЫЙ ПРИМЕР")
    print("=" * 60)
    
    # Создаем тестовый файл
    f_filename = "example_f.txt"
    g_filename = "example_g.txt"
    
    # Создаем тестовые данные
    test_numbers = [15, -8, 0, 23, 42, -17, 6, 99, -4, 10]
    even_numbers = [num for num in test_numbers if num % 2 == 0]
    
    print(f"Тестовые числа: {test_numbers}")
    print(f"Чётные числа: {even_numbers}")
    
    # Записываем тестовые данные в файл f
    with open(f_filename, 'w', encoding='utf-8') as f:
        f.write(" ".join(map(str, test_numbers)))
    
    print(f"\nСоздан файл '{f_filename}'")
    read_and_display_file(f_filename, description="Исходный файл f")
    
    # Фильтруем чётные числа
    print("\nФильтрация чётных чисел...")
    success, even_count, total = filter_even_numbers_v1(f_filename, g_filename)
    
    if success:
        print(f"Успешно отфильтровано {even_count} чётных чисел из {total}")
        read_and_display_file(g_filename, description="Результирующий файл g")
        
        # Проверка корректности
        with open(g_filename, 'r', encoding='utf-8') as g:
            content = g.read()
            if content.strip():
                result_numbers = list(map(int, content.split()))
                if result_numbers == even_numbers:
                    print("✓ Результат корректен!")
                else:
                    print(f"⚠ Ошибка: ожидалось {even_numbers}, получено {result_numbers}")
            else:
                print("Файл g пуст")
    
    # Очистка временных файлов
    if os.path.exists(f_filename):
        os.remove(f_filename)
        print(f"\nУдалён временный файл: {f_filename}")
    
    if os.path.exists(g_filename):
        os.remove(g_filename)
        print(f"Удалён временный файл: {g_filename}")


# Основная программа
if __name__ == "__main__":
    print("ПРОГРАММА ДЛЯ ФИЛЬТРАЦИИ ЧЁТНЫХ ЧИСЕЛ ИЗ ФАЙЛА")
    print("=" * 60)
    
    # Демонстрационный пример
    demonstrate_example()
    
    # Интерактивный режим
    interactive_mode()
    
    print("\n" + "=" * 60)
    print("Программа завершена")
    print("=" * 60)
