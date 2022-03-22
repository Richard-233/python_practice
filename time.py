n = 1618708103123
if __name__ == '__main__':
    n /= 1000
    n %= 24 * 60 * 60
    h = n // (60 * 60)
    m = n % (60 * 60) // 60
    s = n % 60

    if h / 10 < 1:
        h = '0' + str(int(h))
    else:
        h=str(int(h))
    if m / 10 < 1:
        m = '0' + str(int(m))
    else:
        m=str(int(m))
    if s / 10 < 1:
        s = '0' + str(int(s))
    else:
        s=str(int(s))

    print(h+':'+m+':'+s)
