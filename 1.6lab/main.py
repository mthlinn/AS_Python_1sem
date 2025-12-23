s = input("Введите строку: ")
for i in range(len(s)):
    if i % 2 == 0:  # оставляем символы с четными индексами
        result += s[i]

print(result)
