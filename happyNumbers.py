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
            total = 0
            for d in digits:
                total += d**2
            happyNumber(total)
            return False
    ## if we haven't returned false yet, we know the number must be 1, so we append 1 to the list of numbers and return true
    pastNums.append(1)
    return True


def callhappyNumber(number):    
    happy = happyNumber(number)
    if pastNums[-1] == 1:
        print("\n", number, "is a happy number!")
    else:
        print("\n", number, "is not a happy number")



callhappyNumber(44)


