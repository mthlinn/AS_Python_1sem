# Задание 4 из ЕГЭ-2025 профиль [https://math-ege.sdamgia.ru/test?id=86355909]
#Научная конференция проводится в 5 дней. Всего запланировано 75 докладов  — первые три дня по 17 докладов, остальные распределены поровну между четвертым и пятым днями. Порядок докладов определяется жеребьёвкой. Какова вероятность, что доклад профессора М. окажется запланированным на последний день конференции?

def calculate_probability():
    """
    Рассчитывает вероятность того, что доклад профессора М. окажется в последний день
    """
    # Данные из условия
    total_days = 5
    total_reports = 75
    reports_day1_3 = 17  # докладов в каждый из первых трех дней
    reports_day4_5 = (total_reports - 3 * reports_day1_3) / 2  # поровну между 4 и 5 днями
    
    print("АНАЛИЗ УСЛОВИЯ:")
    print(f"Всего дней: {total_days}")
    print(f"Всего докладов: {total_reports}")
    print(f"Докладов в первые 3 дня: по {reports_day1_3} каждый день")
    print(f"Докладов в первые 3 дня всего: {3 * reports_day1_3}")
    print(f"Осталось докладов на 4 и 5 дни: {total_reports - 3 * reports_day1_3}")
    print(f"Докладов в 4-й день: {reports_day4_5}")
    print(f"Докладов в 5-й день: {reports_day4_5}")
    
    # Проверка
    total_check = 3 * reports_day1_3 + 2 * reports_day4_5
    print(f"Проверка общего количества: {total_check} = {total_reports}")
    
    # Вероятность = количество докладов в последний день / общее количество докладов
    probability = reports_day4_5 / total_reports
    
    print(f"\nВЕРОЯТНОСТЬ:")
    print(f"Благоприятные исходы: доклад в последний день = {reports_day4_5}")
    print(f"Все возможные исходы: все доклады = {total_reports}")
    print(f"Вероятность P = {reports_day4_5}/{total_reports} = {probability:.4f}")
    
    return probability

def verify_classical_probability():
    """
    Проверка по классическому определению вероятности
    """
    total_reports = 75
    reports_last_day = 12  # (75 - 3*17) / 2
    
    # Все элементарные события равновероятны (жеребьевка)
    favorable = reports_last_day
    total = total_reports
    
    P = favorable / total
    
    print(f"\nПРОВЕРКА ПО КЛАССИЧЕСКОМУ ОПРЕДЕЛЕНИЮ:")
    print(f"P(A) = m/n, где:")
    print(f"m = число благоприятных исходов = {favorable}")
    print(f"n = общее число исходов = {total}")
    print(f"P = {favorable}/{total} = {P:.4f}")
    
    return P

def main():
    print("РЕШЕНИЕ ЗАДАЧИ О ВЕРОЯТНОСТИ")
    print("=" * 50)
    
    # Основной расчет
    prob1 = calculate_probability()
    
    # Проверка
    prob2 = verify_classical_probability()
    
    # Сокращение дроби
    from fractions import Fraction
    fraction_prob = Fraction(12, 75)
    simplified = fraction_prob.reduce()
    
    print(f"\nОТВЕТ В ВИДЕ ДРОБИ:")
    print(f"Исходная дробь: {fraction_prob}")
    print(f"Сокращенная дробь: {simplified}")
    print(f"Десятичная форма: {float(simplified):.4f}")
    
    print(f"\nФИНАЛЬНЫЙ ОТВЕТ:")
    print(f"Вероятность того, что доклад профессора М. окажется")
    print(f"в последний день конференции: {simplified} ≈ {float(simplified):.4f}")

if __name__ == "__main__":
    main()
