## Square the number, then add the squares of it's resulting digits and repeat until 1

# ex: 7**2 == 49
#     4**2 + 9**2 == 97
#     9**2 + 7**2 == 130
#     1**2 + 3**2 + 0**2 = 10
#     1**2 + 0**2 == 1
#     7 is a happy number!

pastNums = []

def happyNumber(number):
    if number != 1:
        if number in pastNums:
            return False
        else:
            pastNums.append(number)
            digits = [int(d) for d in str(number)]
            # print(digits)
            total = 0
            for d in digits:
                total += d**2
            print(total)
            happyNumber(total)
            return total
    else: 
        return False


def callhappyNumber(number):

    print(number)
    total = happyNumber(number)
    if total == 1:
        print("\n", number, "is a happy number!")
    else:
        print("\n", number, "is not a happy number")



callhappyNumber(2)

# for i in range(10):
#     lst.append(random.randrange(1, 100))

