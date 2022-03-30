import math
n=21
dp = [[0 for j in range(21)] for i in range(n<<21)]
g = [[0 for m in range(22)] for k in range(22)]


for i in range(1, n+1):
    for j in range(1, n+1):
        if math.gcd(i, j) == 1:
            g[i - 1][j - 1] = g[j - 1][i - 1] = 1
dp[1][0] = 1
i = 1  # i表示状态
while i < (1<<n):
    for j in range(n):
        if (i >> j & 1) == 0:
            continue
        if dp[i][j] == 0:
            continue
        for k in range(n):
            if (i >> k & 1) == 0 and g[k][j] == 1:
                dp[i + (1 << k)][k] += dp[i][j]
    i += 1

res = 0
for i in range(n):
    res += dp[(1<<n)- 1][i]
print(res)
