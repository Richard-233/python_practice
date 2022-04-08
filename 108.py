import queue


def dfs(x):
    if index_num[1] == 1:
        if go[x[1]] == 0:
            go[x[1]] = 1
            if index_num[0] != x[0]:
                point.append(x[0])
                index_num[0] = x[0]
            for i in range(num):
                if route[x[1]][i] == 1:
                    if go[x[1]] == 0:
                        q.put([x[1], i])
            dfs(q.get())
    else:
        index_num[1] = 0
        return


if __name__ == '__main__':
    index_num = [-1, 1]
    num = int(input())

    line = [i for i in range(num)]
    route = [[0 for __ in range(num + 1)] for _ in range(num + 1)]
    point = []
    go = [0 for i in range(num + 1)]
    q = queue.Queue(maxsize=num)
    q.put([1, 1])

    for i in range(num):
        a, b = map(int, input().split(' '))
        route[a][b] = route[b][a] = 1

    dfs(q.get())
    print(point)
