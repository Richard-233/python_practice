num = []
i = 1
n = int(input())

while num.count(n) == 0:
    if i == 1:
        num.append(1)
    if i == 2:
        num.extend([1, 1])
    if i>2:
        num1 = [1]
        k = i - 2
        line = 0
        while k != 0:
            line += k
            k -= 1
        for j in range(2, i):
            a = num[line + j - 2]+num[line + j - 1]
            num1.append(a)
        num1.append(1)
        num.extend(num1)
    i += 1
print(num.index(n)+1)
