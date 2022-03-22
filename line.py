def main():
    line = set()
    list = []
    num = 0
    for i in range(20):
        for j in range(21):
            list.append([i, j])
    for i in list:
        num += 1
        for j in list[num:]:
            if i != j and i[0] != j[0]:
                    k = (i[1] - j[1]) / (i[0] - j[0])
                    d = j[1]-k * j[0]
                    line.add((round(k,8), round(d,8)))
    print(len(line) + 20)


if __name__ == '__main__':
    main()
