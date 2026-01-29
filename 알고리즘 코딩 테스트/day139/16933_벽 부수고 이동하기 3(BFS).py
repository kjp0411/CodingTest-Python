# https://www.acmicpc.net/problem/16933
# Python BFS 정석 풀이 → 시간 초과
# 상태 차원 축소 + visited 재정의로 PyPy3 통과
from collections import deque
import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())
graph = [input().rstrip() for _ in range(n)]
visited = [[k + 1 for _ in range(m)] for _ in range(n)]
visited[0][0] = 0

dir = ((1, 0), (-1, 0), (0, 1), (0, -1))

def bfs(start):
    queue = deque()
    queue.append(start)
    ans = 1
    time = True  # True: 낮, False: 밤

    while queue:
        for _ in range(len(queue)):
            i, j, w = queue.popleft()

            if i == n - 1 and j == m - 1:
                print(ans)
                return

            for dy, dx in dir:
                ni, nj = i + dy, j + dx
                if ni < 0 or ni >= n or nj < 0 or nj >= m:
                    continue
                if visited[ni][nj] <= w:
                    continue

                # 빈 칸
                if graph[ni][nj] == '0':
                    visited[ni][nj] = w
                    queue.append((ni, nj, w))

                # 벽
                elif w < k:
                    if not time:  # 밤 → 대기
                        queue.append((i, j, w))
                    else:  # 낮 → 부수고 이동
                        visited[ni][nj] = w + 1
                        queue.append((ni, nj, w + 1))

        ans += 1
        time = not time

    print(-1)

bfs((0, 0, 0))

# 정석 풀이
# import sys
# from collections import deque
#
# input = sys.stdin.readline
#
# N, M, K = map(int, input().strip().split())
# board = [list(map(int, input().strip())) for _ in range(N)]
#
# visited = [[[[-1] * 2 for _ in range(K+1)] for _ in range(M)] for _ in range(N)]
#
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
#
# def bfs():
#     queue = deque()
#     queue.append((0, 0, K, 0, 1))   # (x, y, k, day(낮: 0 밤: 1), dist)
#     visited[0][0][K][0] = 1
#
#     while queue:
#         x, y, k, day, dist = queue.popleft()
#
#         if x == N-1 and y == M-1:
#             return dist
#
#         for d in range(4):
#             nx, ny = x + dx[d], y + dy[d]
#             if 0 <= nx < N and 0 <= ny < M:
#                 # 기준 1: 다음 칸이 벽인지 빈 칸인지
#                 nk = k
#                 nday = (1 - day)
#                 if board[nx][ny] == 0 and visited[nx][ny][nk][nday] == -1:
#                     visited[nx][ny][nk][nday] = (dist+1)
#                     queue.append((nx, ny, nk, nday, dist+1))
#
#                 elif board[nx][ny] == 1:
#                     # 기준 2: 낮인지 밤인지
#                     if day == 0 and k > 0 and visited[nx][ny][k-1][nday] == -1:
#                         visited[nx][ny][k-1][nday] = (dist + 1)
#                         queue.append((nx, ny, k-1, nday, dist + 1))
#
#                     elif day == 1 and k > 0 and visited[x][y][k][nday] == -1:
#                         visited[x][y][k][nday] = (dist + 1)
#                         queue.append((x, y, k, nday, dist + 1))
#
#     return -1
#
# print(bfs())