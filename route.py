import math

distance = [[], []]
n = 2021


#
# def gongyue(a, b):
#     if a < b:
#         temp = a
#         a = b
#         b = temp
#     while b != 0:
#         temp = a % b
#         a = b
#         b = temp
#     return a


def gongbei(a, b):
    return a * b / math.gcd(a, b)


if __name__ == '__main__':
    # for i in range(2, n + 1):
    #     if abs(i - 1) <= 21:
    #         min.append([gongbei(i, 1), -1])
    #     else:
    #         min.append([1000000000000000000000000000000000000000000000000000000000000000000, -1])
    # min[2][1] = 1
    # point = 2
    # num = 2
    # distance = [0, 100000000000000000000000000000000000000000000000000000000000000000000000]
    # while min[n][1] == -1:
    #     num += 1
    #     if min[num][1] == -1:
    #         if min[num][0] < distance[1]:
    #             distance[0] = num
    #             distance[1] = min[num][0]
    #         if abs(num - point) <= 21:
    #             gongbei1 = gongbei(point, num)
    #             if min[num][0] > gongbei1 + min[point][0]:
    #                 min[num][0] = gongbei1 + min[point][0]
    #                 if min[num][0] < distance[1]:
    #                     distance[0] = num
    #                     distance[1] = min[num][0]
    #         if num == n:
    #             point = distance[0]
    #             min[point][1] = 1
    #             num = 2
    #             distance = [0, 100000000000000000000000000000000000000000000000000000000000000000000000]
    # print(int(min[n][0]))

    n = 2021
    distance = [float('inf')] * (n + 1)
    distance[1]=0
    for i in range(1, n):
        for j in range(i+1, i + 22):
            if j>n:
                break
            distance[j] = min(distance[j], distance[i] + gongbei(i, j))
    print(distance[n])
