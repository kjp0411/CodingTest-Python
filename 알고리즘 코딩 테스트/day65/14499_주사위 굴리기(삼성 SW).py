# https://www.acmicpc.net/problem/14499
# 크기가 N*M인 지도가 존재한다.
# 지도의 오른쪽은 동쪽, 위쪽은 북쪽이다.
# 지도의 좌표는 (r, c)로 나타내며, r은 북쪽으로부터 떨어진 칸의 개수, c는 서쪽으로부터 떨어진 칸의 걔수이다.
# 주사위는 지도 위에 윗면이 1이고, 동쪽을 바라보는 방향이 3인 상태이며, 좌표 (x, y)에 위치한다.
# 가장 처음에 주사위에는 모든 면에 0이 적혀져 있다.
# 지도의 각 칸에는 정수가 하나씩 쓰여져 있다.
# 주사위를 굴렸을 때, 이동한 칸에 쓰여 있는 수가 0이면 주사위 바닥면에 쓰여 있는 수가 칸에 복사되며, 칸에 쓰여 있는 수는 0이 된다.
# 주사위를 놓은 곳의 좌표와 이동시키는 명령이 주어졌을 때 주사위가 이동했을 때 마다 상단에 쓰여 있는 값을 구하시오.
# 단, 주사위는 지도의 바깥으로 이동시킬 수 없으며, 바깥으로 이동시려고하는 명령은 무시해야한다.(출력 X)
import sys
input = sys.stdin.readline

N, M, X, Y, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
order = list(map(int, input().split()))

# dice[0] : 윗면
# dice[1] : 아랫면
# dice[2] : 상
# dice[3] : 하
# dice[4] : 좌
# dice[5] : 우
dice = [0, 0, 0, 0, 0, 0]

# 이동 방향 정의
dr = [0, 0, 0, -1, 1]   # 동, 서, 북, 남: 행 변화
dc = [0, 1, -1, 0, 0]   # 동, 서, 북, 남: 열 변화

def roll(d):    # d: 방향 (동쪽은 1, 서쪽은 2, 북쪽은 3, 남쪽은 4)
    top, bottom, north, south, west, east = dice
    if d == 1:      # 동쪽
        # 변화 O
        dice[0] = west
        dice[1] = east
        dice[4] = bottom
        dice[5] = top
        # 변화 X
        dice[2] = north
        dice[3] = south
    elif d == 2:    # 서쪽
        # 변화 O
        dice[0] = east
        dice[1] = west
        dice[4] = top
        dice[5] = bottom
        # 변화 X
        dice[2] = north
        dice[3] = south
    elif d == 3:  # 북쪽
        # 변화 O
        dice[0] = south
        dice[1] = north
        dice[2] = top
        dice[3] = bottom
        # 변화 X
        dice[4] = west
        dice[5] = east
    elif d == 4:  # 남쪽
        # 변화 O
        dice[0] = north
        dice[1] = south
        dice[2] = bottom
        dice[3] = top
        # 변화 X
        dice[4] = west
        dice[5] = east

x, y = X, Y     # 현재 위치

for d in order:
    nx = x + dr[d]
    ny = y + dc[d]

    # 범위 밖이면 명령 무시
    if not (0 <= nx < N and 0 <= ny < M):
        continue

    x, y = nx, ny
    roll(d)

    if board[x][y] == 0:
        board[x][y] = dice[1]
    else:
        dice[1] = board[x][y]
        board[x][y] = 0

    print(dice[0])