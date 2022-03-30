if __name__ == '__main__':
    s = "bb"
    length = len(s)
    maxL = 1
    index = 0
    if length < 2:
        print(s)
    dp = [[False for k in range(length)] for _ in range(length)]
    for l in range(2, length+1):
        for i in range(length):
            j = l + i - 1
            if j >= length:
                break
            if i == j:
                dp[i][j] = True
            if l <= 3 and s[i] == s[j]:
                dp[i][j] = True
            else:
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
            if dp[i][j]:
                if l > maxL:
                    maxL = l
                    index = i
    print(s[index:index + maxL])
