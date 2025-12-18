# https://www.acmicpc.net/problem/21608
import sys
input = sys.stdin.readline

N = int(input())
board = [[0] * N for _ in range(N)]

like = {}
order = []

for _ in range(N * N):
    data = list(map(int, input().split()))
    student = data[0]
    like[student] = set(data[1:])
    order.append(student)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 학생 배치
for student in order:
    candidates = []

    for x in range(N):
        for y in range(N):
            if board[x][y] != 0:
                continue

            like_cnt = 0
            empty_cnt = 0

            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]
                if 0 <= nx < N and 0 <= ny < N:
                    if board[nx][ny] in like[student]:
                        like_cnt += 1
                    elif board[nx][ny] == 0:
                        empty_cnt += 1

            candidates.append((-like_cnt, -empty_cnt, x, y))

    candidates.sort()
    x, y = candidates[0][2], candidates[0][3]
    board[x][y] = student

# 만족도 계산
score = 0
point = [0, 1, 10, 100, 1000]

for x in range(N):
    for y in range(N):
        cnt = 0
        student = board[x][y]
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < N and 0 <= ny < N:
                if board[nx][ny] in like[student]:
                    cnt += 1
        score += point[cnt]

print(score)