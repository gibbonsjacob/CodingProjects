


fibs = []
def fib(x): 
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:

        return fib(x-1) + fib(x-2)

for i in range(20):

    fibs.append(fib(i))

for i in range(len(fibs)):
    print(fibs[i])

