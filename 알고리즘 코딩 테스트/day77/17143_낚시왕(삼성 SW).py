# https://www.acmicpc.net/problem/17143
# Python 3 시간 초과 -> PyPy3 통과
# 낚시왕은 처음에 1번 열의 한 칸 왼쪽에 있다.
# 낚시왕은 가장 오른쪽 열의 오른쪽 칸에 이동하면 이동을 멈춘다.

# 다음은 1초 동안 일어나는 일이며, 아래 적힌 순서대로 일어난다.
# 1.낚시왕이 오른쪽으로 한 칸 이동한다.
# 2.낚시왕이 있는 열에 있는 상어 중에서 땅과 제일 가까운 상어를 잡는다.
# (상어를 잡으면 격자판에서 잡은 상어가 사라진다.)
# 3.상어가 이동한다.

# 낚시왕이 상어 낚시를 하는 격자판의 상태가 주어졌을 때,
# 낚시왕이 잡은 상어 크기의 합을 구하시오.
import sys
input = sys.stdin.readline

R, C, M = map(int, input().split())

board = [[None] * C for _ in range(R)]

for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    board[r-1][c-1] = [s, d, z]

# 방향: 위(1), 아래(2), 오른쪽(3), 왼쪽(4)
dr = [0, -1, 1, 0, 0]
dc = [0, 0, 0, 1, -1]

result = 0

for fisher in range(C):  # 낚시왕이 0~C-1 열까지 이동
    # 1) 가장 가까운 상어 잡기
    for r in range(R):
        if board[r][fisher] is not None:
            result += board[r][fisher][2]  # 크기 더하기
            board[r][fisher] = None
            break

    # 2) 상어 이동
    new_board = [[None] * C for _ in range(R)]

    for r in range(R):
        for c in range(C):
            if board[r][c] is None:
                continue

            s, d, z = board[r][c]

            # 속도 최적화
            if d == 1 or d == 2:
                s %= (R - 1) * 2
            else:
                s %= (C - 1) * 2

            nr, nc, nd = r, c, d

            for _ in range(s):
                nr += dr[nd]
                nc += dc[nd]

                # 경계 체크 -> 방향 반전
                if nr < 0:
                    nr = 1
                    nd = 2
                elif nr >= R:
                    nr = R - 2
                    nd = 1
                if nc < 0:
                    nc = 1
                    nd = 3
                elif nc >= C:
                    nc = C - 2
                    nd = 4

            # 이동 후 보드에 삽입
            if new_board[nr][nc] is None:
                new_board[nr][nc] = [s, nd, z]
            else:
                # 큰 상어만 살아남음
                if new_board[nr][nc][2] < z:
                    new_board[nr][nc] = [s, nd, z]

    # 보드 갱신
    board = new_board

print(result)
