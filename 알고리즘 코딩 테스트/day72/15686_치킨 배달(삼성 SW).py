# https://www.acmicpc.net/problem/15686
# 도시의 크기는 NxN 이다.
# 도시의 각 칸은 빈 칸, 치킨집, 집 중 하나이다.
from itertools import combinations
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

houses = []
chickens = []

for r in range(N):
    for c in range(N):
        if city[r][c] == 1:
            houses.append((r, c))
        elif city[r][c] == 2:
            chickens.append((r, c))

answer = float('inf')

for selected in combinations(chickens, M):
    total_dist = 0
    for hr, hc  in houses:
        dist = min(abs(hr - cr) + abs(hc - cc) for cr, cc in selected)
        total_dist += dist
    answer = min(answer, total_dist)

print(answer)