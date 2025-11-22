# https://www.acmicpc.net/problem/15685
import sys
input = sys.stdin.readline

N = int(input())
visited = [[False] * 101 for _ in range(101)]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

for _ in range(N):
    x, y, d, g = map(int, input().split())

    directions = [d]

    # g 세대까지 방향 생성
    for _ in range(g):
        temp = []
        for dir in reversed(directions):
            temp.append((dir + 1) % 4)
        directions += temp

    # 시작점 체크
    visited[y][x] = True

    # 방향대로 이동하며 체크
    for dir in directions:
        x += dx[dir]
        y += dy[dir]
        visited[y][x] = True

# 정사각형 개수 카운트
answer = 0
for i in range(100):
    for j in range(100):
        if visited[i][j] and visited[i][j + 1] and visited[i + 1][j] and visited[i + 1][j + 1]:
            answer += 1

print(answer)