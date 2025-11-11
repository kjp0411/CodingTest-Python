# https://www.acmicpc.net/problem/2206
# N*M의 행렬, 0: 이동 가능, 1: 이동 불가능(벽)
# (1, 1)에서 (N, M)으로 최단 경로로 이동 예정
# 최단 경로에는 시작하는 칸과 끝나는 칸도 포함해서 count
# 만약에 이동하는 도중에 한 개의 벽을 부수고 이동하는 것이 더 빠르다면 벽 한 개는 부술 수 있음
# 인접한 칸은 상,하,좌,우(대각선 x)
# 도착할 수 없다면 -1 출력
import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())
grid = [list(input().strip()) for _ in range(N)]

# visited[r][c][b] : (r, c)에 '벽 부숨 여부 b' 상태로 방문했는지 확인
visited = [[[False]*2 for _ in range(M)] for _ in range(N)]

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    queue = deque()
    # 시작 칸이 벽일 수도 있다고 가정해 안전 처리
    start_broken = 0
    if grid[0][0] == '1':
        # 시작하자마자 바로 부수고 들어가기(남은 기회 0)
        start_broken = 1

    queue.append((0, 0, start_broken, 1))   # (r, c, broken, dist)
    visited[0][0][start_broken] = True

    while queue:
        r, c, broken, dist = queue.popleft()
        # print(f"[POP] r={r}, c={c}, broken={broken}, dist={dist}")

        if r == N - 1 and c == M - 1:
            return dist

        for i in range(4):
            nr, nc = r + dx[i], c + dy[i]
            if 0 <= nr < N and 0 <= nc < M:
                cell = grid[nr][nc]
                if cell == '0' and not visited[nr][nc][broken]:
                    visited[nr][nc][broken] = True
                    queue.append((nr, nc, broken, dist + 1))
                elif cell == '1' and broken == 0 and not visited[nr][nc][1]:
                    # 아직 한 번도 안 부수고 왔다면 여기서 부수고 진행
                    visited[nr][nc][1] = True
                    queue.append((nr, nc, 1, dist + 1))

    return -1

print(bfs())