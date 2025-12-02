# https://www.acmicpc.net/problem/17837
# 체스판의 크기는 NxN이다.
# 사용하는 말의 개수는 K개이다.
# 말은 원판 모양이며, 하나의 말 위에 다른 말을 올릴 수 있다.
# 체스판의 각 칸은 흰색, 빨간색, 파란색 중 하나이다.
# 게임은 체스판 위에 말 K개를 놓고 시작한다.
# 말은 1번부터 K번까지 번호가 매겨져 있고, 이동 방향도 미리 정해져 있다.
# 이동 방향은 위, 아래, 왼쪽, 오른쪽 4가지 중 하나이다.
#턴 한 번은 1번 말부터 K번 말까지 순서대로 이동시키는 것이다.
# 한 말이 이동할 때 위에 올려져 있는 말도 함께 이동한다.
# 말의 이동 방향에 있는 칸에 따라서 말의 이동이 다르며 아래와 같다.
# 턴이 진행되던 중에 말이 4개 이상 쌓이는 순간 게임이 종료된다.
import sys
input = sys.stdin.readline

dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

# 말 정보: (x, y, 방향)
horses = []
# 각 칸에 쌓여있는 말들
stack = [[[] for _ in range(N)] for _ in range(N)]

for i in range(K):
    x, y, d = map(int, input().split())
    x -= 1
    y -= 1
    horses.append([x, y, d])
    stack[x][y].append(i)

def reverse_dir(d):
    if d == 1: return 2
    if d == 2: return 1
    if d == 3: return 4
    if d == 4: return 3

def move():
    for i in range(K):
        x, y, d = horses[i]
        nx = x + dx[d]
        ny = y + dy[d]

        # 이동 불가 -> 방향 반대로 하고 1번 더 체크
        if not (0 <= nx < N and 0 <= ny < N) or board[nx][ny] == 2:
            nd = reverse_dir(d)
            horses[i][2] = nd
            nx = x + dx[nd]
            ny = y + dy[nd]

            if not (0 <= nx < N and 0 <= ny < N) or board[nx][ny] == 2:
                continue  # 아예 이동 못 함

        # 현재 칸에서 i번 말이 어느 위치인지 찾기
        idx = stack[x][y].index(i)
        moving = stack[x][y][idx:]
        stack[x][y] = stack[x][y][:idx]

        # 흰색
        if board[nx][ny] == 0:
            stack[nx][ny].extend(moving)

        # 빨간색 -> 순서 뒤집기
        elif board[nx][ny] == 1:
            stack[nx][ny].extend(moving[::-1])

        # 이동한 말들의 좌표 업데이트
        for m in moving:
            horses[m][0] = nx
            horses[m][1] = ny

        # 말이 4개 이상 쌓이면 종료
        if len(stack[nx][ny]) >= 4:
            return True

    return False

turn = 0
while turn <= 1000:
    turn += 1
    if move():
        print(turn)
        break

if turn > 1000:
    print(-1)