# https://www.acmicpc.net/problem/17136
import sys
input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(10)]

colorPaper = [0, 5, 5, 5, 5, 5]
result = float('inf')

def can_attach(r, c, size):
    if r + size > 10 or c + size > 10:
        return False
    for i in range(size):
        for j in range(size):
            if board[r+i][c+j] == 0:
                return False
    return True

def attach(r, c, size, value):
    for i in range(size):
        for j in range(size):
            board[r+i][c+j] = value

def dfs(pos, used):
    global result

    if used >= result:
        return

    if pos == 100:
        result = min(result, used)
        return

    r = pos // 10
    c = pos % 10

    if board[r][c] == 0:
        dfs(pos + 1, used)
        return

    attached = False

    for size in range(5, 0, -1):
        if colorPaper[size] > 0 and can_attach(r, c, size):
            attached = True

            attach(r, c, size, 0)
            colorPaper[size] -= 1

            dfs(pos + 1, used + 1)

            attach(r, c, size, 1)
            colorPaper[size] += 1

    if not attached:
        return

dfs(0, 0)

print(result if result != float('inf') else -1)