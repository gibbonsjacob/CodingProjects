from cmath import sqrt
from math import floor
import random
import math
lst = []
primes = []
composites = []




def GetPrimes(num):
    for i in range(2, int(math.sqrt(num))):
        prime = True
        if num % i == 0:
            prime = False
        if prime:
            return True
        else:
            return False

def getFactors(num):
    factors = []
    for i in range(1, num):
        if num % i == 0:
            factors.append(i)
            # if num not in dictFactors.keys():
            #     factors = [i]
            # else:
            #     dictFactors[num].append(i)
    return factors




for i in range(1000):
    lst.append(random.randrange(1, 10000))


for x in sorted(lst):
    if GetPrimes(x):
        primes.append(x)
    else:
        composites.append(x)





for num in composites:
    
    print(num, getFactors(num))    