# вариант 1
s = input()

v = ""
i = 0
n = len(s)
while i < n:
  x = s[i]
  y = 1
while i + 1 < n and s[i+1] == x:
  y += 1
  i += 1
if y == 1 :
  v += x + str(count)
i += 1

len_orig = len(s)
len_v = len(v)

x = None
max_save = -1

i = 0
while i < n:
  x = s[i]
  y = 1
while i + 1 < n and s[i+1] == c:
  y += 1
  i += 1

if y > 1;
rle_legth = 1 + len(str(y))
save = y - rle_legth
  if save > max_save:
    max_save = save
    best_save = x
elif save == max_save
    if x < best_x:
      best_x = x

i += 1
print(len_orig)
print(len_v) 

if best_x is None:
  if s:
    best_x = min(s)
  else:
    best_x = ""
print(best_x)
  
