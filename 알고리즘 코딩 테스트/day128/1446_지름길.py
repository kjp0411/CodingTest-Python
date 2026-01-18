# https://www.acmicpc.net/problem/1446
N, D = map(int, input().strip().split())
dp = []
for i in range(D + 1):
    dp.append(i)

shortcuts = {}
for _ in range(N):
    S, E, L = list(map(int, input().strip().split()))
    if S not in shortcuts:
        shortcuts[S] = []
    if E <= D:
        shortcuts[S].append((E, L))

for x in range(D):
    dp[x+1] = min(dp[x+1], dp[x] + 1)
    if x in shortcuts:
        for E, L in shortcuts[x]:
            dp[E] = min(dp[E], dp[x] + L)

print(dp[D])