# https://www.acmicpc.net/problem/2775
import sys
input = sys.stdin.readline
D = [[0 for j in range(15)] for i in range(15)]

for i in range(1, 15):
    D[i][1] = 1
    D[0][i] = i

for i in range(1, 15):
    for j in range(2, 15):
        D[i][j] = D[i][j - 1] + D[i - 1][j]

T = int(input())

for i in range(0, T):   # D 테이블을 모두 구해 놓은 후 질의에 대한 답 출력
    K = int(input())
    N = int(input())
    print(D[K][N])