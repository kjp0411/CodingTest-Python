# https://www.acmicpc.net/problem/16236
# 공간의 크기는 N x N이며, 물고기 M마리, 아기 상어 1마리가 있다.
# 아기 상어와 물고기는 모두 크기를 가지고 있다.
# (아기 상어의 처읨 크기는 2이다.)
# (아기 상어는 1초에 상하좌우로 인접한 한 칸씩 이동한다.)
# 아기 상어는 자신의 크기보다 큰 물고기가 있는 칸은 지나갈 수 없다.
# (아기 상어는 자신의 크기보다 작은 물고기만 먹을 수 있다.)
# -> 크기가 같은 물고기는 먹을 수는 없지만 칸은 지나갈 수 있다.

# 어디로 이동할지 결정하는 방법
# 더 이상 먹을 수 있는 물고기가 공간에 없다면 아기 상어는 엄마 상어에게 도움을 요청한다.
# 먹을 수 있는 물고기가 1마리라면, 그 물고기를 먹으러 간다.
# 먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운 물고기를 먹으러 간다.
# 거리는 아기 상어가 있는 칸에서 물고기가 있는 칸으로 이동할 때, 지나야하는 칸의 개수의 최솟값이다.
# 거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다.
from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

# 상어 초기 위치
for r in range(N):
    for c in range(N):
        if board[r][c] == 9:
            shark_r, shark_c = r, c
            board[r][c] = 0     # 상어 위치는 빈칸으로 처리해야 BFS
            break

# 상어 기본 정보
size = 2
eat = 0
time = 0

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(sr, sc, size):
    visited = [[False] * N for _ in range(N)]
    q = deque()
    q.append((sr, sc, 0))
    visited[sr][sc] = True

    fishes = []     # 먹을 수 있는 물고기 후보
    min_dist = 1e9

    while q:
        r, c, d = q.popleft()

        if d > min_dist:
            break

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                if board[nr][nc] <= size:
                    visited[nr][nc] = True
                    q.append((nr, nc, d + 1))

                    if 0 < board[nr][nc] < size:
                        fishes.append((nr, nc, d + 1))
                        min_dist = d + 1

    # 먹을 물고기 없으면 None 리턴
    if not fishes:
        return None

    # 정렬
    fishes.sort(key=lambda x: (x[2], x[0], x[1]))
    return fishes[0]

while True:
    target = bfs(shark_r, shark_c, size)

    # 먹을 물고기가 없다면
    if target is None:
        print(time)
        break

    tr, tc, dist = target

    # 상어 이동
    shark_r, shark_c = tr, tc
    time += dist

    # 물고기 먹기
    board[tr][tc] = 0
    eat += 1

    # 크기 증가
    if eat == size:
        size += 1
        eat = 0