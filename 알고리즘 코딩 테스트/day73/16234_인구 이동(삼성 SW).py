# https://www.acmicpc.net/problem/16234
# 땅의 크기는 N x N이다.
# 각각의 땅에는 나라가 하나씩 존재한다.
# 인접한 나라 사이에는 국경선이 존재한다.
# 인구 이동은 하루 동안 진행되고, 인구 이동이 없을 때 까지 지속된다.

# 국경선을 공유하는 두 나라의 인구 차이가 L명 이상, R명 이하라면, 두 나라가 공유하는 국경선을 오늘 하루 동안 연다.
# 위의 조건에 의해 열어야하는 국경선이 모두 열렸다면, 인구 이동을 시작한다.
# 국경선이 열려있어 인접한 칸만을 이용해 이동할 수 있으면, 그 나라를 오늘 하루 동안은 연합이라고 한다.
# 연합을 이루고 있는 각 칸의 인구수는 (연합의 인구수) / (연합을 이루고 있는 칸의 개수)가 된다. 편의상 소수점은 버린다.
# 연합을 해체하고, 모든 국경선을 닫는다.
import sys
from collections import deque
input = sys.stdin.readline

N, L, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

# 상, 하, 좌, 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(sr, sc, visited):
    q = deque()
    q.append((sr, sc))
    visited[sr][sc] = True
    union = [(sr, sc)]
    total = board[sr][sc]

    while q:
        r, c = q.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                # 국경 조건
                if L <= abs(board[r][c] - board[nr][nc]) <= R:
                    visited[nr][nc] = True
                    q.append((nr, nc))
                    union.append((nr, nc))
                    total += board[nr][nc]

    return union, total

days = 0

while True:
    visited = [[False] * N for _ in range(N)]
    moved = False   # 오늘 이동 발생했는지

    for r in range(N):
        for c in range(N):
            if not visited[r][c]:
                union, total = bfs(r, c, visited)
                if len(union) > 1:
                    moved = True
                    new_value = total // len(union)
                    # 인구 재분배
                    for ur, uc in union:
                        board[ur][uc] = new_value

    if not moved:
        break
    days += 1

print(days)