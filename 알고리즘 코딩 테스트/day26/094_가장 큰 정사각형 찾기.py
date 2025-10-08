# https://www.acmicpc.net/problem/1915
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
D = [[0 for j in range(1001)] for i in range(1001)]
max_value = 0

for i in range(0, N):
    numbers = list(input())
    for j in range(0, M):
        D[i][j] = int(numbers[j])
        if D[i][j] == 1 and i > 0 and j > 0:
            D[i][j] = min(D[i - 1][j - 1], D[i - 1][j], D[i][j - 1]) + D[i][j]
        if max_value < D[i][j]:
            max_value = D[i][j]
print(max_value * max_value)