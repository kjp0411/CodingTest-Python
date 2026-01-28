# https://www.acmicpc.net/problem/14442
# Python 3 시간 초과 -> PyPy3 통과
import sys
from collections import deque

input = sys.stdin.readline

N, M, K = map(int, input().strip().split())
board = [list(map(int, input().strip())) for _ in range(N)]
visited = [[[0] * (K+1) for _ in range(M)] for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    queue = deque()
    queue.append((0, 0, K))
    visited[0][0][K] = 1

    while queue:
        x, y, k = queue.popleft()
        d = visited[x][y][k]

        if x == N-1 and y == M-1:
            return d

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                # 벽 부수기
                if board[nx][ny] == 1 and k > 0 and not visited[nx][ny][k - 1]:
                    visited[nx][ny][k - 1] = d + 1
                    queue.append((nx, ny, k - 1))
                # 그냥 이동
                elif board[nx][ny] == 0 and not visited[nx][ny][k]:
                    visited[nx][ny][k] = d + 1
                    queue.append((nx, ny, k))

    return -1

print(bfs())