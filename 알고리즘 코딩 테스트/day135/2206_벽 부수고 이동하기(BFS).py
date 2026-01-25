# https://www.acmicpc.net/problem/2206
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]
visited = [[[-1]*2 for _ in range(M)] for _ in range(N)]

# 상, 하, 좌, 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs():
    queue = deque()
    #시작 칸이 벽인 경우(바로 부셔야 함)
    start_broken = 0

    if board[0][0] == '1':
        start_broken = 1
    queue.append((0, 0, start_broken))
    visited[0][0][start_broken] = 1

    while queue:
        r, c, b = queue.popleft()

        if r == N-1 and c == M-1:
            return visited[r][c][b]

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            if 0 <= nr < N and 0 <= nc < M:
                if board[nr][nc] == '0' and visited[nr][nc][b] == -1:
                    visited[nr][nc][b] = visited[r][c][b] + 1
                    queue.append((nr, nc, b))

                elif board[nr][nc] == '1'and b == 0 and visited[nr][nc][1] == -1:
                    visited[nr][nc][1] = visited[r][c][b] + 1
                    queue.append((nr, nc, 1))
    return -1

print(bfs())