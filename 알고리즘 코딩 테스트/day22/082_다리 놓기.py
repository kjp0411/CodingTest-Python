# https://www.acmicpc.net/problem/1010
import sys
input = sys.stdin.readline
D = [[0 for j in range(31)] for i in range(31)]

for i in range(0, 31):
    D[i][1] = i
    D[i][0] = 1
    D[i][i] = 1

for i in range(2, 31):
    for j in range(1, i):
        D[i][j] = D[i - 1][j] + D[i - 1][j - 1]

T = int(input())

for i in range(0, T):   # D 테이블을 모두 구해 놓은 후 질의에 대한 답 출력
    N, M = map(int, input().split())
    print(D[M][N])