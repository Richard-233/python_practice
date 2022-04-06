##num, kind = map(int, input().split(' '))
##sum = 0
##for i in range(kind):
##    attack = list(map(int, input().split(' ')))
##    sum += (attack[3] + attack[2]) * (attack[1] - attack[0]+1) / 2
##    print(sum)
##print(sum)

num, kind = map(int, input().split(' '))

tree = [0] * num
tree1 = [0] * num
tree2 = [0] * num

for i in range(kind):
    l, r, s, e = map(int, input().split(' '))
    d = (e - s) / (r - l)
    tree[l - 1] += s
    tree[l] += d - s
    if r < num:
        tree[r] -= s + r * d
    if r + 1 < num:
        tree[r + 1] += s + (r - 1) * d
sum1 = 0

for i in range(num):
    sum1 += tree[i]
    tree1[i] = sum1

sum1 = 0
for i in range(num):
    sum1 += tree1[i]
    tree2[i] = int(sum1)
print(sum(tree2))
