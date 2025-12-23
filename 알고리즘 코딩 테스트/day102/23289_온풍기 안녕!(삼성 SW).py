# https://www.acmicpc.net/problem/23289
from collections import deque
import sys
input = sys.stdin.readline

R, C, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]

check_list = []
warm_airs = []

W = int(input())
walls = set()

# 방향 정의 (1~4)
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

# 바람 전파 방향
ndxy = (
    0,
    ((-1, 1), (0, 1), (1, 1)),     # 우
    ((1, -1), (0, -1), (-1, -1)),  # 좌
    ((-1, -1), (-1, 0), (-1, 1)),  # 상
    ((1, 1), (1, 0), (1, -1))      # 하
)

# 벽 검사 테이블
check_wall = (
    0,
    (((0, 0, 0), (-1, 0, 1)), ((0, 0, 1),), ((1, 0, 0), (1, 0, 1))),
    (((1, 0, 0), (1, -1, 1)), ((0, -1, 1),), ((0, 0, 0), (-1, -1, 1))),
    (((0, -1, 1), (0, -1, 0)), ((0, 0, 0),), ((0, 0, 1), (0, 1, 0))),
    (((0, 0, 1), (1, 1, 0)), ((1, 0, 0),), ((0, -1, 1), (1, -1, 0)))
)

# 벽 입력
for _ in range(W):
    x, y, t = map(int, input().split())
    walls.add((x-1, y-1, t))

# 온풍기 / 조사 위치 분리
for i in range(R):
    for j in range(C):
        if board[i][j] == 5:
            check_list.append((i, j))
        elif 1 <= board[i][j] <= 4:
            ni, nj = i + dx[board[i][j]], j + dy[board[i][j]]
            warm_airs.append((ni, nj, board[i][j]))
        board[i][j] = 0


# 1. 온풍기 바람
def heat():
    for x, y, d in warm_airs:
        visited = [[False]*C for _ in range(R)]
        visited[x][y] = True  # 시작점 방문 처리
        q = deque([(x, y, 5)])

        while q:
            cx, cy, temp = q.popleft()
            board[cx][cy] += temp

            if temp == 1:
                continue

            for idx, (dx_, dy_) in enumerate(ndxy[d]):
                nx, ny = cx + dx_, cy + dy_
                if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny]:
                    blocked = False
                    for wx, wy, t in check_wall[d][idx]:
                        if (cx + wx, cy + wy, t) in walls:
                            blocked = True
                            break  # 즉시 중단
                    if not blocked:
                        visited[nx][ny] = True
                        q.append((nx, ny, temp - 1))


# 2. 온도 조절
def adjust_temp():
    global board
    new_board = [[0]*C for _ in range(R)]
    wall_coord = [0, (0, 0, 1), (0, -1, 1), (0, 0, 0), (1, 0, 0)]

    for i in range(R):
        for j in range(C):
            moved = 0
            for d in range(1, 5):
                nx, ny = i + dx[d], j + dy[d]
                if 0 <= nx < R and 0 <= ny < C:
                    if board[i][j] > board[nx][ny]:
                        wx, wy, t = wall_coord[d]
                        if (i + wx, j + wy, t) not in walls:
                            diff = (board[i][j] - board[nx][ny]) // 4
                            new_board[nx][ny] += diff
                            moved += diff
            new_board[i][j] += board[i][j] - moved
    board = new_board


# 3. 테두리 냉각
def cool_border():
    for y in range(C):
        if board[0][y] > 0:
            board[0][y] -= 1
        if board[R-1][y] > 0:
            board[R-1][y] -= 1
    for x in range(1, R-1):
        if board[x][0] > 0:
            board[x][0] -= 1
        if board[x][C-1] > 0:
            board[x][C-1] -= 1


# 4. 온도 검사
def check_temperature():
    return all(board[x][y] >= K for x, y in check_list)


# 5. 시뮬레이션
def solve():
    cnt = 0
    while True:
        cnt += 1
        heat()
        adjust_temp()
        cool_border()
        if check_temperature() or cnt > 100:
            return cnt

print(solve())
