N = int(input())
if N <= 2:
    print(1)
else:
    winner = [1 for _ in range(N + 1)]
    winner[3] = 2

    for i in range(4, N + 1):
        if i % 3 == 0:
            if winner[i - 1] == 2 or winner[i - 2] == 2:
                winner[i] = 1
            else:
                winner[i] = 2
        elif i % 3 == 1:
            if winner[i - 1] == 2 or winner[i - 3] == 2:
                winner[i] = 1
            else:
                winner[i] = 2
        else:
            if winner[i - 1] == 2 or winner[i - 2] == 2 or winner[i - 3] == 2:
                winner[i] = 1
            else:
                winner[i] = 2

    print(winner[-1])