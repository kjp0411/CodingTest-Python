# https://www.acmicpc.net/problem/1138
N = int(input().strip())
A = list(map(int, input().strip().split()))

line = []
for h in range(N, 0, -1):
    line.insert(A[h-1], h)

print(*line)