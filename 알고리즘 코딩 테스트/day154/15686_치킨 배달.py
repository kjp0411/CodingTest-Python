# https://www.acmicpc.net/problem/15686
import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

houses = []
chickens = []

for r in range(N):
    for c in range(N):
        if board[r][c] == 1:
            houses.append((r, c))
        elif board[r][c] == 2:
            chickens.append((r, c))

answer = float('inf')

for selected in combinations(chickens, M):
    total_dist = 0

    for hr, hc in houses:
        dist = min(abs(hr - cr) + abs(hc - cc) for cr, cc in selected)
        total_dist += dist

    answer = min(answer, total_dist)

print(answer)