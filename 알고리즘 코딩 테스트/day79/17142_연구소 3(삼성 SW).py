# https://www.acmicpc.net/problem/17142
# 바이러스는 활성 상태와 비활성 상태가 있다.
# 가장 처음에 모든 바이러스는 비활성 상태이고,
# 활성 상태인 바이러스는 상하좌우로 인접한 모든 빈 칸으로 동시에 복제되며,
# 1초가 걸린다.
# 승원이는 바이러스 M개를 활성 상태로 변경하려고 한다.
# 연구소는 크기가 N×N이다.
import sys
from itertools import combinations
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

viruses = []
empty_cnt = 0    # 빈 칸 개수 (감염해야 하는 곳)

for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            viruses.append((i, j))
        elif board[i][j] == 0:
            empty_cnt += 1

# 빈 칸이 없으면 0초 (이미 다 채워져 있음)
if empty_cnt == 0:
    print(0)
    exit()

def bfs(active):
    visited = [[-1] * N for _ in range(N)]
    q = deque()

    # 활성 바이러스 시작점
    for x, y in active:
        q.append((x, y))
        visited[x][y] = 0

    infect = 0       # 감염된 빈 칸 수
    max_time = 0     # 빈 칸 감염 시간

    while q:
        x, y = q.popleft()

        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny] == -1 and board[nx][ny] != 1:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))

                    # 빈 칸이면 감염 처리 + 시간 업데이트
                    if board[nx][ny] == 0:
                        infect += 1
                        max_time = max(max_time, visited[nx][ny])

                        # 모든 빈 칸 감염 완료 시 바로 종료 → 시간 절약
                        if infect == empty_cnt:
                            return max_time
    return float("inf")   # 감염 실패

answer = float("inf")

for comb in combinations(viruses, M):
    answer = min(answer, bfs(comb))

print(answer if answer != float("inf") else -1)