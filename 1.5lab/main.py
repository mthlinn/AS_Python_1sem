num = [7, 2, 8, 1, 9, 3, 6]
k = int(input("Введите k: "))

selected = sorted([x for x in lst if x < k])
print(selected)
