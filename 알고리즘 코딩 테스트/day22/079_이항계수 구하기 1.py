# https://www.acmicpc.net/problem/11050
import sys
input = sys.stdin.readline
N, K = map(int, input().split())
D = [[0 for j in range(N + 1)] for i in range(N + 1)]

for i in range(0, N + 1):
    D[i][1] = i     # i개 중 1개를 선택하는 경우의 수는 i개
    D[i][0] = 1     # i개 중 1개도 산택하지 않는 경우의 수는 1개
    D[i][i] = 1     # i개 중 i개를 선택하는 경우의 수는 1개

for i in range(2, N + 1):
    for j in range(1, i):
        D[i][j] = D[i - 1][j] + D[i - 1][j - 1]     # 조합 기본 방정식

print(D[N][K])