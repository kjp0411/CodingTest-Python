# https://www.acmicpc.net/problem/14503
# 방의 크기는 N x M 크기이다.
# 청소기는 동, 서, 남, 북 중 하나를 바라보는 방향이 있음
# 방의 각 칸은 좌표(r,c)로 나타낼 수 있음
# 처음에 빈 칸은 전부 청소되지 않는 상태이다.
# 로봇 청소기 동작 순서
# 1. 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
# 2. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
# 2-1. 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
# 2-2. 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
# 3. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우,
# 3-1. 반시계 방향으로 90도 회전한다.
# 3-2. 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
# 3-3. 1번으로 돌아간다.
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
r, c, d = map(int, input().split())
Room = [list(map(int, input().split())) for _ in range(N)]

# d = 0: 북쪽, d = 1: 동쪽, d = 2: 남쪽, d = 3: 서쪽
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

cleaned = 0

while True:
    # 1. 현재 칸이 아직 청소되지 않은 경우 청소
    if Room[r][c] == 0:
        Room[r][c] = 2   # 2를 '청소됨' 표시로 사용
        cleaned += 1

    # 2. 주변 4칸에 청소되지 않는 빈 칸이 있는지 확인
    has_unclean = False
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < M:
            if Room[nr][nc] == 0:
                has_unclean = True
                break

    if not has_unclean:
        # 2번 조건: 주변에 청소할 곳이 없음 -> 후진 시도
        back_d = (d + 2) % 4
        br = r + dr[back_d]
        bc = c + dc[back_d]
        # 2-2. 뒤가 벽이면 종료
        if Room[br][bc] == 1:
            break
        # 2-1. 한 칸 후진(방향은 그대로 유지)
        r, c = br, bc
    else:
        # 3번 조건: 주변에 청소할 곳이 있음 -> 반시계 회전 후 한 칸 전진 시도
        # 3-1. 반시계 방향 90도 회전
        d = (d + 3) % 4
        nr = r + dr[d]
        nc = c + dc[d]
        # 3-2. 앞이 청소되지 않은 빈칸이면 전진
        if 0 <= nr < N and 0 <= nc < M and Room[nr][nc] == 0:
            r, c = nr, nc

print(cleaned)