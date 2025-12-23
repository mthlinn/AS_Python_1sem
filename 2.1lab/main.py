
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged_dict = dict1 | dict2  # или {**dict1, **dict2}
print("а) Объединенный словарь:", merged_dict)

print("\nб) Содержимое словаря:")
for key, value in merged_dict.items():
    print(key, value)

list1 = [1, 2, 3]
list2 = [4, 5, 6]
keys = ['key1', 'key2']
lists = [list1, list2]
result_dict = {keys[i]: lists[i] for i in range(len(keys))}
print("\nв) Словарь из списков:", result_dict)
