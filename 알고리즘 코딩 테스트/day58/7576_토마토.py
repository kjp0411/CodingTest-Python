# https://www.acmicpc.net/problem/7576
# 익지 않은 토마토는 익은 토마토와 인접(상하좌우 O, 대각선 X)한 상태로 하루가 지나면 익음
# 며칠이 지나야 다 익게 되는지 최소 일수 구하기
# 모두 익는 케이스
# -1로 둘러쌓여서 익지 못하는 케이스
# 익은 토마토가 하나도 없는 케이스
# BFS
from collections import deque
import sys
input = sys.stdin.readline

M, N = map(int, input().split())    # M=열, N=행
grid = [list(map(int, input().split())) for _ in range(N)]

queue = deque()
unripe = 0  # 안 익은 토마토 수

# 익은 토마토가 여러 개일 수도 있으니 멀티 소스 + BFS 진행
for r in range(N):
    for c in range(M):
        if grid[r][c] == 1:
            queue.append((r, c))    # 멀티 소스 시작점
        elif grid[r][c] == 0:
            unripe += 1

if unripe == 0:
    print(0)
    sys.exit(0)

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

days = 0
while queue and unripe > 0:
    for _ in range(len(queue)):
        r, c = queue.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < N and 0 <= nc < M and grid[nr][nc] == 0:
                grid[nr][nc] = 1
                unripe -= 1
                queue.append((nr, nc))
    days += 1

print(days if unripe == 0 else -1)