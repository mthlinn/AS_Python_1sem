
A = int(input("Введите A: "))
B = int(input("Введите B: "))

result = 1
for i in range(A, B + 1):
    result *= i

print(result)
