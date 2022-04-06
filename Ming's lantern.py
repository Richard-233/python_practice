# 差分数组：针对数组中一定区间增加变化相同的数
q = '5 3'
w = '2 2 2 1 5'
e = '1 3 3'
r = ['4 5 5']
t = ['1 1 -100']

# 时间复杂度太高
# length, op_num = map(int, input().split(' '))
# lantern = list(map(int, input().split(' ')))
# for i in range(op_num):
#     op = list(map(int, input().split(' ')))
#     for j in range(op[0] - 1, op[1]):
#         lantern[j] += op[2]
#         if lantern[j] < 0:
#             lantern[j] = 0
# for k in lantern:
#     print(k, end=' ')

length, op_num = map(int, input().split(' '))
lantern = list(map(int, input().split(' ')))
op = []
num = 0
for i in range(0, len(lantern)):
    if i == 0:
        op.append(lantern[i])
    else:
        op.append(lantern[i] - lantern[i - 1])
for j in range(op_num):
    o = list(map(int, input().split(' ')))
    op[o[0] - 1] += o[2]
    if o[1] < len(lantern):
        op[o[1]] -= o[2]
for k in range(len(lantern)):
    num += op[k]
    print(max(num, 0), end=" ")
