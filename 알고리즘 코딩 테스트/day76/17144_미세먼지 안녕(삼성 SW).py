# https://www.acmicpc.net/problem/17144
# 1초 동안 아래 적힌 일이 순서대로 일어난다.
# 미세먼지가 확산된다. 확산은 미세먼지가 있는 모든 칸에서 동시에 일어난다.
# (r, c)에 있는 미세먼지는 인접한 네 방향으로 확산된다.
# 인접한 방향에 공기청정기가 있거나, 칸이 없으면 그 방향으로는 확산이 일어나지 않는다.
# 확산되는 양은 Ar,c/5이고 소수점은 버린다. 즉, ⌊Ar,c/5⌋이다.
# (r, c)에 남은 미세먼지의 양은 Ar,c - ⌊Ar,c/5⌋×(확산된 방향의 개수) 이다.

# 공기청정기가 작동한다.
# 공기청정기에서는 바람이 나온다.
# 위쪽 공기청정기의 바람은 반시계방향으로 순환하고, 아래쪽 공기청정기의 바람은 시계방향으로 순환한다.
# 바람이 불면 미세먼지가 바람의 방향대로 모두 한 칸씩 이동한다.
# 공기청정기에서 부는 바람은 미세먼지가 없는 바람이고, 공기청정기로 들어간 미세먼지는 모두 정화된다.
import sys
input = sys.stdin.readline

R, C, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]

# 공기청정기 찾기
cleaner = []
for i in range(R):
    if board[i][0] == -1:
        cleaner.append(i)

def spread():
    temp = [[0]*C for _ in range(R)]
    up, down = cleaner
    temp[up][0] = temp[down][0] = -1

    for r in range(R):
        for c in range(C):
            if board[r][c] > 0:
                amount = board[r][c] // 5
                cnt = 0
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < R and 0 <= nc < C and board[nr][nc] != -1:
                        temp[nr][nc] += amount
                        cnt += 1
                temp[r][c] += board[r][c] - amount * cnt

    return temp

def operate():
    up, down = cleaner

    # 위쪽(반시계)
    for r in range(up-1, 0, -1):
        board[r][0] = board[r-1][0]
    for c in range(C-1):
        board[0][c] = board[0][c+1]
    for r in range(up):
        board[r][C-1] = board[r+1][C-1]
    for c in range(C-1, 1, -1):
        board[up][c] = board[up][c-1]
    board[up][1] = 0

    # 아래쪽(시계)
    for r in range(down+1, R-1):
        board[r][0] = board[r+1][0]
    for c in range(C-1):
        board[R-1][c] = board[R-1][c+1]
    for r in range(R-1, down, -1):
        board[r][C-1] = board[r-1][C-1]
    for c in range(C-1, 1, -1):
        board[down][c] = board[down][c-1]
    board[down][1] = 0

for _ in range(T):
    board = spread()
    operate()

ans = 0
for r in range(R):
    for c in range(C):
        if board[r][c] > 0:
            ans += board[r][c]

print(ans)