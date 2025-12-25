# https://www.acmicpc.net/problem/23291
from collections import deque
from copy import deepcopy

N, K = map(int, input().split())
fish_bowls = deque(map(int, input().split()))
square = []
board = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def add_fishes():
    min_index = []
    minimum = 1e9
    for i, fishes in enumerate(fish_bowls):
        if fishes < minimum:
            min_index = [i]
            minimum = fishes
        elif fishes == minimum:
            min_index.append(i)

    for i in min_index:
        fish_bowls[i] += 1

def stack():
    global square
    square.append([fish_bowls.popleft()])

def turn_right():
    global square
    height = len(square) + 1
    while height <= len(fish_bowls) - len(square[0]):
        #1. 밑변 잘라서 합치기
        tmp = []
        for _ in range(len(square[0])):
            tmp.append(fish_bowls.popleft())
        square.append(tmp)

        #2. 우회전
        new = [[x[i] for x in reversed(square)] for i in range(len(square[0]))]
        square = new

        height = len(square) + 1

def mk_board():
    global board
    board = [[0 for _ in range(len(fish_bowls))] for _ in range(len(square) + 1)]
    for i in range(len(square)):
        for j in range(len(square[0])):
            board[i][j] = square[i][j]
    board[-1] = fish_bowls

def adjust():
    global board
    tmp = deepcopy(board)
    for x in range(len(board)):
        for y in range(len(board[0])):
            if board[x][y] == 0:
                continue
            for d in range(4):
                nx, ny = dx[d] + x, dy[d] + y
                if 0 <= nx < len(board) and 0 <= ny < len(board[0]):
                    if board[nx][ny] != 0:
                        k = (board[x][y] - board[nx][ny]) // 5
                        if k > 0:
                            tmp[x][y] -= k
                            tmp[nx][ny] += k
    board = tmp

def flatten():
    global fish_bowls
    tmp = deque()
    for j in range(len(board[0])):
        for i in range(len(board)-1, -1, -1):
            if board[i][j] == 0:
                break
            tmp.append(board[i][j])
    fish_bowls = tmp

def turn_right2():
    global board
    square = deque()
    for _ in range(N//2):
        square.append(fish_bowls.popleft())

    square.reverse()

    tmp1 = []
    tmp2 = []
    for _ in range(N//4):
        tmp1.append(square.popleft())
        tmp2.append(fish_bowls.popleft())

    new = [tmp1, tmp2]
    for _ in range(2):
        new = [[x[i] for x in reversed(new)] for i in range(len(new[0]))]
    new.append(list(square))
    new.append(list(fish_bowls))
    board = new

def debug():
    for i in range(len(board)):
        for j in range(len(board[0])):
            print(board[i][j], end=" ")
        print()
    print()

def solve():
    cnt = 1
    global square
    while True:
        add_fishes()
        stack()
        turn_right()
        mk_board()
        adjust()
        flatten()
        turn_right2()
        adjust()
        flatten()
        if max(fish_bowls) - min(fish_bowls) <= K:
            return cnt
        square = []
        cnt += 1

print(solve())