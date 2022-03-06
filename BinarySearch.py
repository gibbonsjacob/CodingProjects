import random
from re import search
lst = []
searchLst1 = []
searchLst2 = []
for i in range(100):
    lst.append(random.randrange(1, 10000))


lst = sorted(lst)



for i in range(int(len(lst) / 2)):
    searchLst1.append(lst[i])
    searchLst2.append(lst[i + 50])


