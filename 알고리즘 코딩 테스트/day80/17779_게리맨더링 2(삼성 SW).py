# https://www.acmicpc.net/problem/17779
# 재현시의 크기는 N×N이다.
# 구역을 다섯 개의 선거구로 나눠야 하고, 각 구역은 다섯 선거구 중 하나에 포함되어야 한다.
# 선거구는 구역을 적어도 하나 포함해야 하고, 한 선거구에 포함되어 있는 구역은 모두 연결되어 있어야 한다.
# 구역 A에서 인접한 구역을 통해서 구역 B로 갈 수 있을 때, 두 구역은 연결되어 있다고 한다.
# 중간에 통하는 인접한 구역은 0개 이상이어야 하고, 모두 같은 선거구에 포함된 구역이어야 한다.
import sys
input = sys.stdin.readline

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

answer = 10**18

def divide(x, y, d1, d2):
    board = [[0] * N for _ in range(N)]

    # 5번 경계선 그리기
    for i in range(d1 + 1):
        board[x + i][y - i] = 5
        board[x + d2 + i][y + d2 - i] = 5
    for i in range(d2 + 1):
        board[x + i][y + i] = 5
        board[x + d1 + i][y - d1 + i] = 5

    # 5번 구역 내부 채우기(좌→우, 첫 5 ~ 마지막 5)
    for r in range(x, x + d1 + d2 + 1):
        tmp = []
        for c in range(N):
            if board[r][c] == 5:
                tmp.append(c)
        if len(tmp) == 2:
            for c in range(tmp[0], tmp[1] + 1):
                board[r][c] = 5

    population = [0] * 5

    # 1번 구역
    for r in range(0, x + d1):
        for c in range(0, y + 1):
            if board[r][c] == 5:
                break
            population[0] += A[r][c]

    # 2번 구역
    for r in range(0, x + d2 + 1):
        for c in range(N - 1, y, -1):
            if board[r][c] == 5:
                break
            population[1] += A[r][c]

    # 3번 구역
    for r in range(x + d1, N):
        for c in range(0, y - d1 + d2):
            if board[r][c] == 5:
                break
            population[2] += A[r][c]

    # 4번 구역
    for r in range(x + d2 + 1, N):
        for c in range(N - 1, y - d1 + d2 - 1, -1):
            if board[r][c] == 5:
                break
            population[3] += A[r][c]

    # 5번 구역
    s = sum(map(sum, A))
    population[4] = s - sum(population[:4])

    return max(population) - min(population)


# 가능한 모든 (x, y, d1, d2) 탐색
for x in range(N):
    for y in range(N):
        for d1 in range(1, N):
            for d2 in range(1, N):
                # 조건: 경계가 지도 밖으로 나가면 안 됨
                if x + d1 + d2 >= N:
                    continue
                if y - d1 < 0 or y + d2 >= N:
                    continue

                answer = min(answer, divide(x, y, d1, d2))

print(answer)
