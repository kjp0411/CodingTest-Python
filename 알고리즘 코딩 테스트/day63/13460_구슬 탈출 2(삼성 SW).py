# https://www.acmicpc.net/problem/13460
# 구슬 탈출은 직사각형 보드에 빨간 구슬과 파란 구슬을 1개씩 넣은 다음에 빨간 구슬을 구멍을 통해 빼내는 게임
# 보드의 세로는 N 가로는 M이고 가장 바깥 행과 열은 모두 막혀져 있고 보드에는 구멍이 하나 있다.
# 구슬은 상, 하, 좌, 우(네 가지 동작)로 기울이기가 가능하다.(동작을 멈추는 것은 구슬이 더 이상 움직이지 않을 때 까지이다.)
# 각각의 동작에서 공은 동시에 움직인다.
# 성공 조건: 파란 구슬은 구멍에 빠지면 안되고 빨간 구슬만 빠지면 성공
# 실패 조건: 파란 구슬이 구멍에 빠지면 실패
# 실패 조건: 빨간 구슬과 파란 구슬이 동시에 구멍에 빠져도 실패
# 단, 빨간 구슬과 파란 구슬은 동시에 같은 칸에 있을 수 없다.
# 보드의 상태가 주어졌을 때, 최소 몇 번 만에 빨간 구슬을 구멍을 통해 빼낼 수 있는지 구하시오
import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]

rx = ry = bx = by = 0

# 초기 구슬 위치 찾기
for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            rx, ry = i, j
            board[i][j] = '.'   # 빈 칸으로 바꿔두기
        elif board[i][j] == 'B':
            bx, by = i, j
            board[i][j] = '.'


def move(x, y, dx, dy):
    cnt = 0
    # 다음 칸이 벽이 아니고, 아직 구멍에 안 빠졌으면 계속 이동
    while board[x + dx][y + dy] != '#' and board[x][y] != 'O':
        x += dx
        y += dy
        cnt += 1
        # 구멍에 도착 했다면
        if board[x][y] == 'O':
            break
    return x, y, cnt

visited = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]

queue = deque()
queue.append((rx, ry, bx, by, 0))
visited[rx][ry][bx][by] = True

# 상, 하, 좌, 우
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

answer = -1

while queue:
    rx, ry, bx, by, depth = queue.popleft()

    # 10번 이하로 움직여서 빨간 구슬을 빼내야 하고 못 빼내면 실패
    if depth >= 10:
        continue

    for dx, dy in dirs:
        nrx, nry, rcnt = move(rx, ry, dx, dy)
        nbx, nby, bcnt = move(bx, by, dx, dy)

        # 파란 구슬이 먼저 구멍에 빠진 경우: 실패
        if board[nbx][nby] == 'O':
            continue

        # 빨간 구슬만 구멍에 빠진 경우: 성공
        if board[nrx][nry] == 'O':
            answer = depth + 1
            queue.clear()
            break

        # 둘 다 구멍에 안 빠졌는데 위치가 같다면, 더 멀리 움직인 구술을 한 칸 뒤로
        if nrx == nbx and nry == nby:
            if rcnt > bcnt:
                nrx -= dx
                nry -= dy
            else:
                nbx -= dx
                nby -= dy

        if not visited[nrx][nry][nbx][nby]:
            visited[nrx][nry][nbx][nby] = True
            queue.append((nrx, nry, nbx, nby, depth + 1))

print(answer)