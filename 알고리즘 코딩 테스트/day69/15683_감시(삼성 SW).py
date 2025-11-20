# https://www.acmicpc.net/problem/15683
# 사무실의 크기는 NxM 크기의 직사각형으로 나타낼 수 있다.
# 사무실에는 총 K개의 CCTV가 있으며 CCTV의 종류는 5가지가 있다.
# 1번: 한 쪽 방향만 감시 가능
# 2번(서로 반대 방향), 3번(직각 방향): 두 방향 감시 가능
# 4번: 세 방향 감시 가능
# 5번: 네 방향 감시 가능
# 사무실에는 벽이 있는데 벽은 통과할 수 없다.
# CCTV가 감시할 수 없는 영역은 사각지대다.
# CCTV는 회전시킬 수 있는데, 회전은 90도 방향으로 해야 하며,
# 감시하려고 하는 방향이 가로 또는 세로 방향이어야 한다.
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
office = [list(map(int, input().split())) for _ in range(N)]

cctvs = []
for r in range(N):
    for c in range(M):
        if 1 <= office[r][c] <= 5:
            cctvs.append((r, c, office[r][c]))

dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]

directions = {
    1: [[0], [1], [2], [3]],
    2: [[0, 2], [1, 3]],
    3: [[0, 1], [1, 2], [2, 3], [3, 0]],
    4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    5: [[0, 1, 2, 3]]
}

def watch(board, r, c, d):
    nr, nc = r + dr[d], c + dc[d]
    while 0 <= nr < N and 0 <= nc < M:
        if board[nr][nc] == 6:
            break
        if board[nr][nc] == 0:
            board[nr][nc] = '#'
        nr += dr[d]
        nc += dc[d]

answer = 1e9

def dfs(idx, board):
    global answer

    # 모든 CCTV 방향 선택 완료
    if idx == len(cctvs):
        blind = sum(row.count(0) for row in board)
        answer = min(answer, blind)
        return

    r, c, type = cctvs[idx]

    # 해당 CCTV의 모든 방향 조합 시도
    for dirs in directions[type]:
        new_board = [row[:] for row in board]
        for d in dirs:
            watch(new_board, r, c, d)
        dfs(idx + 1, new_board)

dfs(0, office)
print(answer)