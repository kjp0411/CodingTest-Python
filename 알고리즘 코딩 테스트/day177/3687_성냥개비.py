# https://www.acmicpc.net/problem/3687
dp = [""] * 101

dp[2] = "1"
dp[3] = "7"
dp[4] = "4"
dp[5] = "2"
dp[6] = "6"
dp[7] = "8"

digit = ["", "", "1", "7", "4", "2", "0", "8"]

for i in range(8, 101):
    candidates = []

    for j in range(2, 8):
        if i - j >= 2:
            candidates.append(dp[i - j] + digit[j])

    dp[i] = min(candidates, key=lambda x: (len(x), x))

T = int(input())

for _ in range(T):
    N = int(input())

    min_num = dp[N]

    if N % 2 == 0:
        max_num = "1" * (N // 2)
    else:
        max_num = "7" + "1" * ((N - 3) // 2)

    print(min_num, max_num)