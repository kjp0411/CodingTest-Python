# https://www.acmicpc.net/problem/20057
import sys
input = sys.stdin.readline

N = int(input())
desert = [list(map(int, input().split())) for _ in range(N)]

answer = 0
now = [N // 2, N // 2]  # 현재 위치

# 왼쪽 기준 (정수 퍼센트)
left = [
    (-2, 0, 2), (2, 0, 2),
    (-1, -1,10), (-1, 0, 7), (-1, 1, 1),
    (1, -1,10),  (1, 0, 7),  (1, 1, 1),
    (0, -2, 5)
]

right = [(x, -y, z) for x, y, z in left]
down  = [(-y, x, z) for x, y, z in left]
up    = [(-x, y, z) for x, y, z in down]

rate = {
    'left': left,
    'right': right,
    'down': down,
    'up': up
}

# 이동 함수
def move(cnt, dx, dy, direction):
    global answer
    for _ in range(cnt + 1):
        now[0] += dx
        now[1] += dy

        x, y = now
        sand = desert[x][y]
        desert[x][y] = 0   # 현재 칸 모래 제거
        spread = 0

        for rx, ry, r in rate[direction]:
            amount = sand * r // 100
            spread += amount
            nx, ny = x + rx, y + ry
            if 0 <= nx < N and 0 <= ny < N:
                desert[nx][ny] += amount
            else:
                answer += amount

        # alpha
        ax, ay = x + dx, y + dy
        remain = sand - spread
        if 0 <= ax < N and 0 <= ay < N:
            desert[ax][ay] += remain
        else:
            answer += remain

        # 종료 조건
        if x == 0 and y == 0:
            print(answer)
            sys.exit()

# 달팽이 이동
for i in range(N):
    if i % 2 == 0:
        move(i, 0, -1, 'left')
        move(i, 1, 0, 'down')
    else:
        move(i, 0, 1, 'right')
        move(i, -1, 0, 'up')