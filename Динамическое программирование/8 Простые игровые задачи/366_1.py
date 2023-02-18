N = int(input())
if N == 1 or N == 2:
    print(1)
elif N == 3:
    print(2)
else:
    dp = [1] * (N + 1)
    dp[3] = 2

    for i in range(4, N + 1):
        if i % 3 == 0:
            if dp[i - 1] == 2 or dp[i - 2] == 2:
                dp[i] = 1
            else:
                dp[i] = 2
        elif i % 3 == 1:
            if dp[i - 1] == 2 or dp[i - 3] == 2:
                dp[i] = 1
            else:
                dp[i] = 2
        else:
            if dp[i - 1] == 2 or dp[i - 2] == 2 or dp[i - 3] == 2:
                dp[i] = 1
            else:
                dp[i] = 2
    print(dp[N])
