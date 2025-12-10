# https://www.acmicpc.net/problem/19236
import sys
import copy
input = sys.stdin.readline

# 방향: 1~8 → 문제 정의 그대로 사용
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

answer = 0

def move_fish(board, fish, sx, sy):
    # 물고기 1~16 이동
    for i in range(1, 17):
        if fish[i][0] == -1:
            continue  # 죽은 물고기

        x, y, d = fish[i]

        for rot in range(8):
            nd = (d + rot) % 8
            nx = x + dx[nd]
            ny = y + dy[nd]

            # 범위 밖 or 상어면 이동 불가
            if nx < 0 or nx >= 4 or ny < 0 or ny >= 4:
                continue
            if nx == sx and ny == sy:
                continue

            # 교환 대상 물고기
            target = board[nx][ny]

            # 보드 내 교환
            board[x][y], board[nx][ny] = board[nx][ny], board[x][y]

            # fish 정보 업데이트
            fish[i] = [nx, ny, nd]
            if target != 0:
                fish[target][0], fish[target][1] = x, y

            break


def dfs(board, fish, sx, sy, sd, total):
    global answer

    # 정답 갱신
    answer = max(answer, total)

    # 1. 물고기 이동
    move_fish(board, fish, sx, sy)

    # 2. 상어 이동 (1~3칸 직진)
    for step in range(1, 4):
        nx = sx + dx[sd] * step
        ny = sy + dy[sd] * step

        # 범위 밖이면 이동 불가
        if nx < 0 or nx >= 4 or ny < 0 or ny >= 4:
            break

        if board[nx][ny] == 0:
            continue  # 빈칸이면 이동 불가

        # 새로운 상태 복사
        new_board = copy.deepcopy(board)
        new_fish = copy.deepcopy(fish)

        # 물고기 먹기
        target = new_board[nx][ny]
        nd = new_fish[target][2]  # 방향 상속

        # 상어 이동 전 물고기 제거
        new_fish[target] = [-1, -1, -1]
        new_board[nx][ny] = -1
        new_board[sx][sy] = 0

        dfs(new_board, new_fish, nx, ny, nd, total + target)


# 입력 처리
board = [[0]*4 for _ in range(4)]
fish = [[-1, -1, -1] for _ in range(17)]

for i in range(4):
    data = list(map(int, input().split()))
    for j in range(4):
        num = data[2*j]
        d = data[2*j + 1] - 1  # 0~7로 변환
        board[i][j] = num
        fish[num] = [i, j, d]

# 초기 상어 이동
first = board[0][0]
sd = fish[first][2]
fish[first] = [-1, -1, -1]
board[0][0] = -1

dfs(board, fish, 0, 0, sd, first)
print(answer)
