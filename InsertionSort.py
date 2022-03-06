import random 



lst = []

for i in range(100):
    lst.append(random.randrange(1, 10000))

for i in range(1, len(lst)):
    if lst[i] < lst[i-1]:
        lst[i], lst[i-1] = lst[i-1], lst[i]