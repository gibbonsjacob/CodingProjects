import random

lst = []

for i in range(100):
    lst.append(random.randrange(1, 10000))



n = len(lst)
for i in range(n):
    for j in range(0, n - i - 1):
        if lst[j] > lst[j + 1]:
            lst[j], lst[j +1] = lst[j +1], lst[j]

print(lst)
