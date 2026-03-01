# https://www.acmicpc.net/problem/2631
N = int(input())
students = []

for _ in range(N):
    students.append(int(input()))

dp = [1] * N

for i in range(N):
    for j in range(i):
        if students[j] < students[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(N - max(dp))