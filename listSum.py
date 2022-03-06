import random
lst = []
target = 12

def listSum(target, lst):
    for i in range(len(lst)):
        newTarget = target - lst[i]
        if newTarget in lst:
            if lst[i] != newTarget or lst.count(newTarget) > 1:
                return True
    return False


def calllistSum():
    for i in range(10):
        lst.append(random.randrange(1, 10))
    Correct = listSum(target, lst)
    print(lst, target, Correct)


calllistSum()