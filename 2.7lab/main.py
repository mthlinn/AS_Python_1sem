import os
import tempfile
import shutil


def replace_empty_lines_with_string_v1(file_path, replacement_string):
    """
    Заменяет все пустые строки в файле на заданную строку S.
    Версия 1: Чтение всего файла в память.
    
    Параметры:
    file_path (str): путь к файлу
    replacement_string (str): строка S для замены пустых строк
    
    Возвращает:
    bool: True, если операция успешна, иначе False
    
    Примечание: Пустой строкой считается строка, содержащая только символы пробела,
    табуляции или перевод строки (т.е. strip() возвращает пустую строку).
    """
    try:
        # Проверка существования файла
        if not os.path.exists(file_path):
            print(f"Ошибка: файл '{file_path}' не найден")
            return False
        
        # Проверка, что файл является файлом
        if not os.path.isfile(file_path):
            print(f"Ошибка: '{file_path}' не является файлом")
            return False
        
        # Чтение файла
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        # Замена пустых строк
        modified_lines = []
        empty_lines_count = 0
        
        for line in lines:
            if line.strip() == '':  # Проверка на пустую строку
                modified_lines.append(replacement_string + '\n')
                empty_lines_count += 1
            else:
                modified_lines.append(line)
        
        # Запись изменений обратно в файл
        with open(file_path, 'w', encoding='utf-8') as file:
            file.writelines(modified_lines)
        
        print(f"Успешно заменено {empty_lines_count} пустых строк на '{replacement_string}'")
        return True
        
    except PermissionError:
        print(f"Ошибка: недостаточно прав для записи в файл '{file_path}'")
        return False
    except UnicodeDecodeError:
        print(f"Ошибка: не удается декодировать файл '{file_path}' как UTF-8")
        return False
    except Exception as e:
        print(f"Неизвестная ошибка: {e}")
        return False


def replace_empty_lines_with_string_v2(file_path, replacement_string):
    """
    Заменяет все пустые строки в файле на заданную строку S.
    Версия 2: Использование временного файла для безопасности.
    
    Параметры:
    file_path (str): путь к файлу
    replacement_string (str): строка S для замены пустых строк
    
    Возвращает:
    bool: True, если операция успешна, иначе False
    """
    try:
        # Проверка существования файла
        if not os.path.exists(file_path):
            print(f"Ошибка: файл '{file_path}' не найден")
            return False
        
        if not os.path.isfile(file_path):
            print(f"Ошибка: '{file_path}' не является файлом")
            return False
        
        # Создаем временный файл
        with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', delete=False, 
                                       suffix='.tmp') as temp_file:
            temp_path = temp_file.name
            
            # Открываем исходный файл и временный файл
            with open(file_path, 'r', encoding='utf-8') as source_file:
                empty_lines_count = 0
                
                for line in source_file:
                    if line.strip() == '':  # Пустая строка
                        temp_file.write(replacement_string + '\n')
                        empty_lines_count += 1
                    else:
                        temp_file.write(line)
        
        # Заменяем исходный файл временным
        shutil.move(temp_path, file_path)
        
        print(f"Успешно заменено {empty_lines_count} пустых строк на '{replacement_string}'")
        return True
        
    except PermissionError:
        print(f"Ошибка: недостаточно прав для работы с файлом '{file_path}'")
        # Удаляем временный файл, если он существует
        if 'temp_path' in locals() and os.path.exists(temp_path):
            os.remove(temp_path)
        return False
    except UnicodeDecodeError:
        print(f"Ошибка: не удается декодировать файл '{file_path}' как UTF-8")
        if 'temp_path' in locals() and os.path.exists(temp_path):
            os.remove(temp_path)
        return False
    except Exception as e:
        print(f"Неизвестная ошибка: {e}")
        if 'temp_path' in locals() and os.path.exists(temp_path):
            os.remove(temp_path)
        return False


def replace_empty_lines_with_string_v3(file_path, replacement_string, keep_whitespace_only=False):
    """
    Заменяет все пустые строки в файле на заданную строку S.
    Версия 3: Расширенная с дополнительными параметрами.
    
    Параметры:
    file_path (str): путь к файлу
    replacement_string (str): строка S для замены пустых строк
    keep_whitespace_only (bool): если True, строки, содержащие только пробелы,
                                 не считаются пустыми и не заменяются
    
    Возвращает:
    tuple: (success, empty_lines_count, total_lines)
    """
    success = False
    empty_lines_count = 0
    total_lines = 0
    
    try:
        # Проверка существования файла
        if not os.path.exists(file_path):
            print(f"Ошибка: файл '{file_path}' не найден")
            return (False, 0, 0)
        
        if not os.path.isfile(file_path):
            print(f"Ошибка: '{file_path}' не является файлом")
            return (False, 0, 0)
        
        # Получаем информацию о файле (размер, дата изменения)
        file_stats = os.stat(file_path)
        print(f"Файл: {file_path}")
        print(f"Размер: {file_stats.st_size} байт")
        
        # Читаем и обрабатываем файл
        lines = []
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                total_lines += 1
                
                if keep_whitespace_only:
                    # Строка считается пустой, если она полностью пустая
                    # (даже без пробелов)
                    is_empty = (line == '\n' or line == '\r\n' or line == '')
                else:
                    # Строка считается пустой, если после удаления
                    # пробельных символов она пустая
                    is_empty = (line.strip() == '')
                
                if is_empty:
                    lines.append(replacement_string + '\n')
                    empty_lines_count += 1
                else:
                    lines.append(line)
        
        # Записываем обратно только если были изменения
        if empty_lines_count > 0:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.writelines(lines)
        
        success = True
        
    except PermissionError:
        print(f"Ошибка: недостаточно прав для записи в файл '{file_path}'")
    except UnicodeDecodeError:
        print(f"Ошибка: не удается декодировать файл '{file_path}' как UTF-8")
        print("Попробуйте указать другую кодировку.")
    except Exception as e:
        print(f"Неизвестная ошибка: {type(e).__name__}: {e}")
    
    return (success, empty_lines_count, total_lines)


def create_test_file(file_path, content_lines):
    """
    Создает тестовый файл с заданным содержимым.
    
    Параметры:
    file_path (str): путь к файлу
    content_lines (list): список строк для записи
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            for line in content_lines:
                file.write(line + '\n')
        print(f"Создан тестовый файл: {file_path}")
        return True
    except Exception as e:
        print(f"Ошибка при создании файла: {e}")
        return False


def display_file_content(file_path, max_lines=20):
    """
    Отображает содержимое файла.
    
    Параметры:
    file_path (str): путь к файлу
    max_lines (int): максимальное количество строк для отображения
    """
    try:
        if not os.path.exists(file_path):
            print(f"Файл '{file_path}' не найден")
            return
        
        print(f"\nСодержимое файла '{file_path}':")
        print("-" * 50)
        
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            
            if len(lines) == 0:
                print("(файл пуст)")
                return
            
            for i, line in enumerate(lines[:max_lines]):
                line_num = i + 1
                # Заменяем непечатаемые символы для лучшего отображения
                display_line = line.rstrip('\n').replace('\t', '\\t').replace('\r', '\\r')
                
                if line.strip() == '':
                    print(f"{line_num:3}: [ПУСТАЯ СТРОКА]")
                else:
                    print(f"{line_num:3}: {display_line}")
            
            if len(lines) > max_lines:
                print(f"... и еще {len(lines) - max_lines} строк")
        
        print("-" * 50)
        
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")


def analyze_file_empty_lines(file_path):
    """
    Анализирует файл и подсчитывает пустые строки.
    
    Параметры:
    file_path (str): путь к файлу
    
    Возвращает:
    tuple: (total_lines, empty_lines, empty_percentage)
    """
    try:
        if not os.path.exists(file_path):
            return (0, 0, 0)
        
        total_lines = 0
        empty_lines = 0
        
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                total_lines += 1
                if line.strip() == '':
                    empty_lines += 1
        
        percentage = (empty_lines / total_lines * 100) if total_lines > 0 else 0
        
        return (total_lines, empty_lines, percentage)
        
    except Exception as e:
        print(f"Ошибка при анализе файла: {e}")
        return (0, 0, 0)


def interactive_mode():
    """
    Интерактивный режим работы программы.
    """
    print("=" * 60)
    print("ЗАМЕНА ПУСТЫХ СТРОК В ФАЙЛЕ")
    print("=" * 60)
    
    while True:
        print("\nМеню:")
        print("1. Заменить пустые строки в существующем файле")
        print("2. Создать тестовый файл и заменить пустые строки")
        print("3. Показать содержимое файла")
        print("4. Анализировать файл (подсчет пустых строк)")
        print("5. Выход")
        
        choice = input("\nВыберите действие (1-5): ").strip()
        
        if choice == '1':
            # Замена пустых строк в существующем файле
            file_path = input("Введите путь к файлу: ").strip()
            replacement_string = input("Введите строку для замены пустых строк: ").strip()
            
            if not file_path or not replacement_string:
                print("Ошибка: путь к файлу и строка замены не могут быть пустыми")
                continue
            
            print("\nВыберите метод:")
            print("1. Быстрый метод (чтение всего файла в память)")
            print("2. Безопасный метод (с временным файлом)")
            print("3. Расширенный метод")
            
            method_choice = input("Ваш выбор (1-3): ").strip()
            
            print("\n" + "=" * 40)
            
            if method_choice == '1':
                success = replace_empty_lines_with_string_v1(file_path, replacement_string)
            elif method_choice == '2':
                success = replace_empty_lines_with_string_v2(file_path, replacement_string)
            elif method_choice == '3':
                keep_whitespace = input("Сохранять строки из пробелов? (y/n): ").lower() == 'y'
                success, count, total = replace_empty_lines_with_string_v3(
                    file_path, replacement_string, keep_whitespace)
                if success:
                    print(f"Успешно заменено {count} из {total} строк")
            else:
                print("Неверный выбор метода")
                continue
            
            if success:
                display_file_content(file_path)
        
        elif choice == '2':
            # Создание тестового файла
            file_path = input("Введите путь для создания тестового файла: ").strip()
            
            if not file_path:
                print("Ошибка: путь к файлу не может быть пустым")
                continue
            
            # Создаем тестовое содержимое
            test_content = [
                "Первая строка",
                "",  # Пустая строка
                "Третья строка",
                "   ",  # Строка с пробелами
                "\t\t",  # Строка с табуляцией
                "Шестая строка",
                "",  # Еще одна пустая строка
                "Последняя строка"
            ]
            
            if create_test_file(file_path, test_content):
                print("\nТестовый файл создан:")
                display_file_content(file_path)
                
                replacement_string = input("\nВведите строку для замены пустых строк: ").strip()
                
                if replacement_string:
                    print("\nЗаменяем пустые строки...")
                    success = replace_empty_lines_with_string_v1(file_path, replacement_string)
                    
                    if success:
                        print("\nРезультат:")
                        display_file_content(file_path)
        
        elif choice == '3':
            # Показать содержимое файла
            file_path = input("Введите путь к файлу: ").strip()
            
            if not file_path:
                print("Ошибка: путь к файлу не может быть пустым")
                continue
            
            display_file_content(file_path)
        
        elif choice == '4':
            # Анализ файла
            file_path = input("Введите путь к файлу: ").strip()
            
            if not file_path:
                print("Ошибка: путь к файлу не может быть пустым")
                continue
            
            total, empty, percentage = analyze_file_empty_lines(file_path)
            
            print(f"\nАнализ файла '{file_path}':")
            print(f"  Всего строк: {total}")
            print(f"  Пустых строк: {empty}")
            print(f"  Процент пустых строк: {percentage:.1f}%")
            
            if empty > 0:
                print(f"\nРекомендация: можно заменить {empty} пустых строк")
        
        elif choice == '5':
            print("Выход из программы...")
            break
        
        else:
            print("Неверный выбор. Попробуйте снова.")


def batch_process_files(file_paths, replacement_string, method='v1'):
    """
    Пакетная обработка нескольких файлов.
    
    Параметры:
    file_paths (list): список путей к файлам
    replacement_string (str): строка для замены
    method (str): метод обработки ('v1', 'v2', 'v3')
    
    Возвращает:
    dict: словарь с результатами обработки каждого файла
    """
    results = {}
    
    print(f"\nПакетная обработка {len(file_paths)} файлов...")
    print(f"Строка замены: '{replacement_string}'")
    print("=" * 50)
    
    for i, file_path in enumerate(file_paths, 1):
        print(f"\n{i}. Обработка файла: {file_path}")
        
        try:
            if method == 'v1':
                success = replace_empty_lines_with_string_v1(file_path, replacement_string)
                results[file_path] = {'success': success}
            elif method == 'v2':
                success = replace_empty_lines_with_string_v2(file_path, replacement_string)
                results[file_path] = {'success': success}
            elif method == 'v3':
                success, count, total = replace_empty_lines_with_string_v3(
                    file_path, replacement_string)
                results[file_path] = {
                    'success': success,
                    'replaced': count,
                    'total': total
                }
            
            if results[file_path].get('success', False):
                # Анализируем результат
                total, empty, percentage = analyze_file_empty_lines(file_path)
                results[file_path]['after_analysis'] = {
                    'total': total,
                    'empty': empty,
                    'percentage': percentage
                }
                
                if empty == 0:
                    print(f"  ✓ В файле больше нет пустых строк")
                else:
                    print(f"  ⚠ В файле осталось {empty} пустых строк ({percentage:.1f}%)")
        
        except Exception as e:
            print(f"  ✗ Ошибка: {e}")
            results[file_path] = {'success': False, 'error': str(e)}
    
    # Сводка результатов
    print("\n" + "=" * 50)
    print("СВОДКА РЕЗУЛЬТАТОВ:")
    successful = sum(1 for r in results.values() if r.get('success', False))
    print(f"Успешно обработано: {successful}/{len(file_paths)}")
    
    return results


# Примеры использования
def demonstrate_examples():
    """
    Демонстрация примеров использования функций.
    """
    print("=" * 60)
    print("ДЕМОНСТРАЦИЯ РАБОТЫ ПРОГРАММЫ")
    print("=" * 60)
    
    # Создаем временный тестовый файл
    import tempfile
    
    # Пример 1: Простая замена
    print("\nПример 1: Простая замена пустых строк")
    
    with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', delete=False, suffix='.txt') as tmp:
        tmp_path = tmp.name
        tmp.write("""Строка 1

Строка 2
   
Строка 3

Строка 4
""")
    
    print(f"Создан тестовый файл: {tmp_path}")
    display_file_content(tmp_path)
    
    # Заменяем пустые строки
    replace_empty_lines_with_string_v1(tmp_path, "[ПУСТАЯ СТРОКА ЗАМЕНЕНА]")
    
    print("\nПосле замены:")
    display_file_content(tmp_path)
    
    # Удаляем временный файл
    os.remove(tmp_path)
    print(f"\nВременный файл удален: {tmp_path}")
    
    # Пример 2: Работа с разными типами пустых строк
    print("\n" + "=" * 40)
    print("Пример 2: Разные типы 'пустых' строк")
    
    with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', delete=False, suffix='.txt') as tmp:
        tmp_path2 = tmp.name
        tmp.write("""Обычная строка

\t\t\t

   \t  

Еще одна строка
""")
    
    print(f"\nИсходный файл:")
    display_file_content(tmp_path2)
    
    print("\nПосле замены (со строками из пробелов):")
    replace_empty_lines_with_string_v1(tmp_path2, "[ЗАМЕНА]")
    display_file_content(tmp_path2)
    
    # Очистка
    os.remove(tmp_path2)


# Основная программа
if __name__ == "__main__":
    print("ПРОГРАММА ДЛЯ ЗАМЕНЫ ПУСТЫХ СТРОК В ФАЙЛЕ")
    print("=" * 60)
    
    # Демонстрация примеров
    demonstrate_examples()
    
    # Интерактивный режим
    interactive_mode()
    
    print("\n" + "=" * 60)
    print("Программа завершена")
    print("=" * 60)
