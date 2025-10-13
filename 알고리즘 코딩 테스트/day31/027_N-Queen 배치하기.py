# https://www.acmicpc.net/problem/9663
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
cnt = 0

cols = [False] * N              # 열 충돌 체크
diag1 = [False] * (2 * N - 1)   # ↗ 대각선 체크 (row + col)
diag2 = [False] * (2 * N - 1)   # ↘ 대각선 체크 (row - col + N - 1)
def backtrack(row):
    global cnt
    if row == N:
        cnt += 1
        return
    for col in range(N):
        if not cols[col] and not diag1[row + col] and not diag2[row - col + N - 1]:
            cols[col] = diag1[row + col] = diag2[row - col + N - 1] = True
            backtrack(row + 1)
            cols[col] = diag1[row + col] = diag2[row - col + N - 1] = False

backtrack(0)
print(cnt)