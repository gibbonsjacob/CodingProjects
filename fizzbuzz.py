import random


lst = []
dictFizzBuzz = {}
for i in range(100):
    lst.append(random.randrange(1, 10000))


for x in sorted(lst):
    fizz = x % 3 == 0
    buzz = x % 5 == 0
    fizzbuzz = fizz and buzz

    if fizzbuzz:
        dictFizzBuzz[str(x)] = 'fizzbuzz'
    elif buzz:
        dictFizzBuzz[str(x)] = 'buzz'
    elif fizz:
        dictFizzBuzz[str(x)] = 'fizz'

    else:
        dictFizzBuzz[str(x)] = ''


for key in dictFizzBuzz.keys():
    print(key, dictFizzBuzz[key])

