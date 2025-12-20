# https://www.acmicpc.net/problem/21610
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
moves = [tuple(map(int, input().split())) for _ in range(M)]

# 방향: 1~8
dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]

# 대각선 방향 (물복사버그)
diag = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

# 초기 구름
clouds = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]

for d, s in moves:
    visited = [[False]*N for _ in range(N)]
    new_clouds = []

    # 1. 구름 이동
    for x, y in clouds:
        nx = (x + dx[d]*s) % N
        ny = (y + dy[d]*s) % N
        new_clouds.append((nx, ny))

    clouds = new_clouds

    # 2. 비 내리기
    for x, y in clouds:
        A[x][y] += 1
        visited[x][y] = True

    # 3. 물복사버그
    for x, y in clouds:
        cnt = 0
        for dx_, dy_ in diag:
            nx, ny = x + dx_, y + dy_
            if 0 <= nx < N and 0 <= ny < N and A[nx][ny] > 0:
                cnt += 1
        A[x][y] += cnt

    # 4. 구름 제거 후 5. 새 구름 생성
    clouds = []
    for i in range(N):
        for j in range(N):
            if A[i][j] >= 2 and not visited[i][j]:
                A[i][j] -= 2
                clouds.append((i, j))

# 결과 출력
print(sum(map(sum, A)))