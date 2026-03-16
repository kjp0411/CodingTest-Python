# https://www.acmicpc.net/problem/1826
import heapq
import sys

input = sys.stdin.readline
N = int(input())
gas_stations = []
for _ in range(N):
    a, b = map(int, input().split())
    gas_stations.append((a, b))
gas_stations.sort()
L, P = map(int, input().split())

heap = []
idx = 0
count = 0

while P < L:
    while idx < N and gas_stations[idx][0] <= P:
        heapq.heappush(heap, -gas_stations[idx][1])
        idx += 1

    if not heap:
        print(-1)
        exit()

    fuel = -heapq.heappop(heap)
    P += fuel
    count += 1

print(count)