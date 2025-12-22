import os
import re

# а) Обработка файла с использованием исключений FileNotFoundError и EOFError
def open_file_a(filename):
    try:
        # Проверка существования файла
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            
            # Проверка на пустой файл
            if not content.strip():
                raise EOFError("Файл пустой")
                
            print("Файл успешно открыт")
            return content
            
    except FileNotFoundError:
        print("Файл не найден")
    except EOFError as e:
        print(str(e))

# б) Проверка строки на URL-адрес
def check_url(string):
    # Простой паттерн для проверки URL
    url_pattern = re.compile(
        r'^(https?|ftp)://'  # протокол
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # домен
        r'localhost|'  # localhost
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # или IP
        r'(?::\d+)?'  # порт
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    
    try:
        if not url_pattern.match(string):
            raise ValueError("Строка не является URL-адресом")
        print("Строка является URL-адресом")
        return True
    except ValueError as e:
        print(str(e))
        return False

# в) Обработка файла с использованием assert
def open_file_c(filename):
    try:
        # Проверка существования файла с помощью assert
        assert os.path.exists(filename), "Файл не найден"
        
        # Проверка размера файла
        if os.path.getsize(filename) == 0:
            raise EOFError("Файл пустой")
        
        # Открываем файл
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            print("Файл успешно открыт")
            return content
            
    except AssertionError as e:
        print(str(e))
    except EOFError as e:
        print(str(e))
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")

# Пример использования функций
if __name__ == "__main__":
    print("=== Часть а) ===")
    open_file_a("example.txt")  # Файл не найден
    open_file_a("empty.txt")    # Файл пустой (если файл существует и пуст)
    
    print("\n=== Часть б) ===")
    check_url("https://www.example.com")  # Строка является URL-адресом
    check_url("не_адрес")                  # Строка не является URL-адресом
    
    print("\n=== Часть в) ===")
    open_file_c("example.txt")  # Файл не найден
    open_file_c("empty.txt")    # Файл пустой (если файл существует и пуст)
