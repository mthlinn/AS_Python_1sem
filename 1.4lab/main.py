
num = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

min_val = min(num)
max_val = max(num)
min_index = num.index(min_val)
max_index = num.index(max_val)

start = min(min_index, max_index) + 1
end = max(min_index, max_index)

for i in range(start, end):
    num[i] = 0

print(num)
