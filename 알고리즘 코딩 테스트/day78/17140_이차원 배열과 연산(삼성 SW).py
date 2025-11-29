# https://www.acmicpc.net/problem/17140
# 배열 A의 크기는 3x3이다.
# 배열의 인덱스는 1부터 시작한다.
# 1초가 지날 때마다 배열에 연산이 적용된다.
# R 연산: 배열 A의 모든 행에 대해서 정렬을 수행한다. 행의 개수 ≥ 열의 개수인 경우에 적용된다.
# C 연산: 배열 A의 모든 열에 대해서 정렬을 수행한다. 행의 개수 < 열의 개수인 경우에 적용된다.
from sys import stdin
input = stdin.readline

A = [[0] * 101 for _ in range(101)]
r, c, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(3)]

for i in range(3):
    for j in range(3):
        A[i+1][j+1] = board[i][j]

row_size, col_size = 3, 3

def R_operation():
    global row_size, col_size, A

    new_max_col = 0
    for i in range(1, row_size + 1):
        counter = {}
        for j in range(1, col_size + 1):
            if A[i][j] != 0:
                counter[A[i][j]] = counter.get(A[i][j], 0) + 1

        nums = sorted(counter.items(), key=lambda x: (x[1], x[0]))

        new_row = []
        for num, cnt in nums:
            new_row += [num, cnt]

        new_row = new_row[:100]

        # 초기화 후 대입
        for j in range(1, 101):
            A[i][j] = 0
        for j in range(len(new_row)):
            A[i][j + 1] = new_row[j]

        new_max_col = max(new_max_col, len(new_row))

    col_size = new_max_col

def C_operation():
    global row_size, col_size, A

    new_max_row = 0
    for j in range(1, col_size + 1):
        counter = {}
        for i in range(1, row_size + 1):
            if A[i][j] != 0:
                counter[A[i][j]] = counter.get(A[i][j], 0) + 1

        nums = sorted(counter.items(), key=lambda x: (x[1], x[0]))

        new_col = []
        for num, cnt in nums:
            new_col += [num, cnt]

        new_col = new_col[:100]

        # 초기화 후 대입
        for i in range(1, 101):
            A[i][j] = 0
        for i in range(len(new_col)):
            A[i + 1][j] = new_col[i]

        new_max_row = max(new_max_row, len(new_col))

    row_size = new_max_row

for t in range(101):
    if A[r][c] == k:
        print(t)
        break

    if row_size >= col_size:
        R_operation()
    else:
        C_operation()
else:
    print(-1)