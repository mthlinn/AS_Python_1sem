
n = int(input("Введите n: "))

result = 0
current_factorial = 1

for i in range(1, n + 1):
    current_factorial *= i
    if i % 2 == 1:
        result += current_factorial
    else:        
        result -= current_factorial

print("result")
