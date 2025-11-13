# https://www.acmicpc.net/problem/13549
# 수빈이와 동생은 숨바꼭질을 하고 있음
# 수빈이의 위치는 점 N(0 <= N <= 100,000)
# 동생의 위치는 점 K(0 <= K <= 100,000)
# 수빈이는 걷거나 순간이동이 가능하다.
# 만약 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동 가능
# 순간이동을 하는 경우에는 0초 후에 2*X의 위치로 이동 가능
# 수빈이가 동생을 찾을 수 있는 가장 빠른 시간을 구하기
from collections import deque

MAX = 100000
N, K = map(int, input().split())
INF = 10**9

dist = [INF] * (MAX + 1)
dist[N] = 0

queue = deque()
queue.append(N)

while queue:
    x = queue.popleft()

    if x == K:
        break

    # 순간 이동: 0초
    nx = x * 2
    if 0 <= nx <= MAX and dist[nx] > dist[x]:
        dist[nx] = dist[x]
        queue.appendleft(nx)

    # 뒤로 1칸 이동: 1초
    nx = x - 1
    if 0 <= nx <= MAX and dist[nx] > dist[x] + 1:
        dist[nx] = dist[x] + 1
        queue.append(nx)

    # 앞으로 1칸 이동: 1초
    nx = x + 1
    if 0 <= nx <= MAX and dist[nx] > dist[x] + 1:
        dist[nx] = dist[x] + 1
        queue.append(nx)

print(dist[K])