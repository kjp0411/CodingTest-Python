# https://www.acmicpc.net/problem/1012
# 배추 근처에 지렁이를 배치해서 배추를 보호
# 지렁이는 인접(상하좌우)한 다른 배추로 이동이 가능
import sys
from collections import deque

input = sys.stdin.readline

# 상, 하, 좌, 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
def bfs(sr, sc):
    queue = deque([(sr, sc)])
    visited[sr][sc] = True
    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < N and 0 <= nc < M:
                if not visited[nr][nc] and field[nr][nc] == 1:
                    visited[nr][nc] = True
                    queue.append((nr, nc))

T = int(input().strip())

for _ in range(T):
    M, N, K = map(int, input().split())
    field = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        field[y][x] = 1

    cnt = 0
    for r in range(N):
        for c in range(M):
            if field[r][c] == 1 and not visited[r][c]:
                bfs(r, c)
                cnt += 1

    print(cnt)