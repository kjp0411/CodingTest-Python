# https://www.acmicpc.net/problem/20056
import sys
input = sys.stdin.readline

# 방향: 0~7 (상, 우상, 우, 우하, 하, 좌하, 좌, 좌상)
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

N, M, K = map(int, input().split())

fireballs = []
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    fireballs.append([r - 1, c - 1, m, s, d])  # 0-index 변환

for _ in range(K):
    board = [[[] for _ in range(N)] for _ in range(N)]

    # 파이어볼 이동
    for r, c, m, s, d in fireballs:
        nr = (r + dr[d] * s) % N
        nc = (c + dc[d] * s) % N
        board[nr][nc].append([m, s, d])

    fireballs = []

    # 합치기 & 분리
    for i in range(N):
        for j in range(N):
            if not board[i][j]:
                continue

            if len(board[i][j]) == 1:
                m, s, d = board[i][j][0]
                fireballs.append([i, j, m, s, d])
            else:
                total_m = sum(x[0] for x in board[i][j])
                total_s = sum(x[1] for x in board[i][j])
                count = len(board[i][j])

                new_m = total_m // 5
                if new_m == 0:
                    continue

                new_s = total_s // count

                # 방향 홀짝 판단
                parity = [x[2] % 2 for x in board[i][j]]
                if all(p == parity[0] for p in parity):
                    new_dirs = [0, 2, 4, 6]
                else:
                    new_dirs = [1, 3, 5, 7]

                for d in new_dirs:
                    fireballs.append([i, j, new_m, new_s, d])

answer = sum(fb[2] for fb in fireballs)
print(answer)