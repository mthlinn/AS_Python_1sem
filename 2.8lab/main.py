
with open('f.txt', 'r') as f:
    numbers = list(map(int, f.read().split()))

even_numbers = [str(x) for x in numbers if x % 2 == 0]

with open('g.txt', 'w') as g:
    g.write(' '.join(even_numbers))
