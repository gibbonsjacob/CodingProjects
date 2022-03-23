import sys

def leibniz(iterations):
    total = 1
    totals = []
    step = -1

    for i in range(iterations):
        denom = (i * 2) + 3
        total += (1 / (step * denom))
        totals.append(4 * total)
        step *= -1


    print(totals[-1])


if __name__ == '__main__':
    leibniz(int(sys.argv[1]))
