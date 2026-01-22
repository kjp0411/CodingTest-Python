# https://www.acmicpc.net/problem/1697
from collections import deque
N, K = map(int, input().strip().split())
def bfs(N, K):
    T = 0
    queue = deque()
    queue.append((N, T))

    visited = [False] * 100001
    visited[N] = True

    while queue:
        cur, time = queue.popleft()
        next_positions = [cur - 1, cur + 1, cur * 2]
        if cur == K:
            return time

        for nxt in next_positions:
            if 0 <= nxt <= 100000:
                if not visited[nxt]:
                    visited[nxt] = True
                    queue.append((nxt, time + 1))

print(bfs(N, K))