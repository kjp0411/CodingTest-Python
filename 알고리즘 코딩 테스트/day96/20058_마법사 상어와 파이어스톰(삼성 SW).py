# https://www.acmicpc.net/problem/20058
import sys
from collections import deque

input = sys.stdin.readline

# 입력
N, Q = map(int, input().split())
size = 2 ** N
board = [list(map(int, input().split())) for _ in range(size)]
levels = list(map(int, input().split()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 부분 격자 회전
def rotate(L):
    sub = 2 ** L
    new_board = [[0] * size for _ in range(size)]

    for x in range(0, size, sub):
        for y in range(0, size, sub):
            for i in range(sub):
                for j in range(sub):
                    new_board[x + j][y + sub - 1 - i] = board[x + i][y + j]

    return new_board

# 얼음 녹이기
def melt():
    melt_list = []

    for x in range(size):
        for y in range(size):
            if board[x][y] == 0:
                continue

            cnt = 0
            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]
                if 0 <= nx < size and 0 <= ny < size and board[nx][ny] > 0:
                    cnt += 1

            if cnt < 3:
                melt_list.append((x, y))

    for x, y in melt_list:
        board[x][y] -= 1

# 가장 큰 덩어리 BFS
def largest_ice():
    visited = [[False] * size for _ in range(size)]
    max_block = 0

    for i in range(size):
        for j in range(size):
            if board[i][j] > 0 and not visited[i][j]:
                q = deque()
                q.append((i, j))
                visited[i][j] = True
                cnt = 1

                while q:
                    x, y = q.popleft()
                    for d in range(4):
                        nx, ny = x + dx[d], y + dy[d]
                        if 0 <= nx < size and 0 <= ny < size:
                            if board[nx][ny] > 0 and not visited[nx][ny]:
                                visited[nx][ny] = True
                                q.append((nx, ny))
                                cnt += 1

                max_block = max(max_block, cnt)

    return max_block

# 파이어스톰 실행
for L in levels:
    board = rotate(L)
    melt()

total_ice = sum(map(sum, board))
largest = largest_ice()

print(total_ice)
print(largest)
