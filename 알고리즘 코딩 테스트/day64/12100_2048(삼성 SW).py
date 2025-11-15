# https://www.acmicpc.net/problem/12100
# 2048 게임의 보드 크기는 NxN 크기이다.
# 한 번의 이동은 보드 위에 있는 전체 블록을 상하좌우 네 방향 중 하나로 이동하는 것이다.
# 이동을 했을 때 같은 값을 갖는 두 블록이 충돌하면 두 블록은 하나로 합쳐진다.
# 한 번의 이동에서 이미 합쳐진 블록은 또 합쳐지지는 않는다.
# 똑같은 수가 3개 있는 경우에는 이동하려고하는 쪽의 칸이 먼저 합쳐진다.
# 최대 5번의 이동을 통해 만들 수 있는 가장 큰 수를 구하시오.
import sys

input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

# 한 줄을 합치는 보조 함수
def compress(line):
    # 0 지우고 숫자만 앞으로 모으기
    tmp = [x for x in line if x != 0]

    result = []
    i = 0
    while i < len(tmp):
        # 바로 옆 숫자랑 같으면 한 번만 합치기
        if i + 1 < len(tmp) and tmp[i] == tmp[i + 1]:
            result.append(tmp[i] * 2)
            i += 2
        else:
            result.append(tmp[i])
            i += 1
    # 나머지는 0으로 채우기
    result += [0] * (N - len(result))
    return result

def move(board, direction):
    # 새 보드에 결과 저장 (원본은 건드리지 않게)
    new_board = [[0] * N for _ in range(N)]

    # 0: 상, 1: 하, 2: 좌, 3: 우
    # 상
    if direction == 0:
        for c in range(N):
            col = [board[r][c] for r in range(N)]
            new_col = compress(col)
            for r in range(N):
                new_board[r][c] = new_col[r]

    # 하
    elif direction == 1:
        for c in range(N):
            col = [board[r][c] for r in range(N - 1, -1, -1)]
            new_col = compress(col)
            new_col.reverse()
            for r in range(N):
                new_board[r][c] = new_col[r]

    # 좌
    elif direction == 2:
        for r in range(N):
            row = board[r]
            new_row = compress(row)
            new_board[r] = new_row

    # 우
    else:
        for r in range(N):
            row = list(reversed(board[r]))
            new_row = compress(row)
            new_row.reverse()
            new_board[r] = new_row

    return new_board

answer = 0

def dfs(board, depth):
    global answer
    max_block = max(map(max, board))
    answer = max(answer, max_block)

    if depth == 5:
        return

    for d in range(4):
        next_board = move(board, d)
        dfs(next_board, depth + 1)

dfs(board, 0)
print(answer)