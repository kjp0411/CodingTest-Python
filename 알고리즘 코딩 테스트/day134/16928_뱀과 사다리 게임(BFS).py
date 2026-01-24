# https://www.acmicpc.net/problem/16928
from collections import deque
N, M = map(int, input().strip().split())
ladder_and_snake = {}

for _ in range(N+M):
    x, y = map(int, input().split())
    ladder_and_snake[x] = y

visited = [-1] * 101
dice = [1, 2, 3, 4, 5, 6]

def bfs():
    queue = deque()
    queue.append(1)
    visited[1] = 0

    while queue:
        cur = queue.popleft()
        if cur == 100:
            return visited[cur]

        for i in range(6):
            nx = cur + dice[i]
            if nx > 100:
                continue

            if nx in ladder_and_snake:
                nx = ladder_and_snake[nx]

            if visited[nx] == -1:
                visited[nx] = visited[cur] + 1
                queue.append(nx)

print(bfs())