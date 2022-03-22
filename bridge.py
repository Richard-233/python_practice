import datetime
import math

n = 21
num = 0


def routes(i, num):
    for j in range(2, n + 1):
        if i!=j and min[i][j] == 1 and route[j] == 0:
            route[j] = 1
            num += 1
            routes(j, num)
            if route.count(0) == 0:
                return


if __name__ == '__main__':
    min = [[0 for i in range(1, n + 2)] for j in range(1, n + 2)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i != j:
                if int(math.gcd(i, j)) == 1:
                    min[i][j] = min[j][i] = 1

    for i in range(2, n + 1):
        route = [1]*2+[0] * (n + 1)
        route[i]=1
        routes(i, num)
    print(num)

    datetime.datetime

