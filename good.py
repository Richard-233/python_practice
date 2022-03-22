# class Main:
#     def __init__(self):
#         self.num = 0
#         self.factor = []
#         self.n = 2021041820210418
#         self.i = 1
#
#     def main(self):
#         while self.i * self.i <= self.n:
#             if self.n % self.i == 0:
#                 self.factor.append(self.i)
#                 if self.i != self.n / self.i:
#                     self.factor.append(int(self.n / self.i))
#                 else:
#                     break
#             self.i += 1
#         print(self.factor)
#         for item1 in self.factor:
#             for item2 in self.factor:
#                 if item1 * item2 > self.n:
#                     continue
#                 for item3 in self.factor:
#                     if item1 * item2 * item3 == self.n:
#                         self.num += 1
#         print(self.num)
#
#
# if __name__ == '__main__':
#     main = Main()
#     main.main()

n = 2021041820210418

res = []

for i in [2, 3]:
    while n != 1:
        if n % i == 0:
            res.append(i)
            n //= i
        else:
            break

for i in range(1, int(n ** 0.5 // 6 + 2)):
    item1 = i * 6 - 1
    item2 = i * 6 + 1
    for j in [item1, item2]:
        while n != 1:
            if n % j == 0:
                res.append(j)
                n //= j
            else:
                break

if n != 1:
    res.append(n)

sets = set()


def dfs(row, x, y, z):
    if row == len(res):
        return sets.add((x, y, z))
    dfs(row + 1, x * res[row], y, z)
    dfs(row + 1, x, y * res[row], z)
    dfs(row + 1, x, y, z * res[row])


dfs(0, 1, 1, 1)

print(len(sets))
