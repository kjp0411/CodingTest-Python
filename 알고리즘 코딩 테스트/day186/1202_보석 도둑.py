# https://www.acmicpc.net/problem/1202
import heapq
import sys

input = sys.stdin.readline
N, K = map(int, input().split())

jewels = []
bags = []

for _ in range(N):
    M, V = map(int, input().split())
    jewels.append((M, V))
for _ in range(K):
    bags.append(int(input()))

jewels.sort()
bags.sort()

heap = []
idx = 0
result = 0

for bag in bags:
    while idx < N and jewels[idx][0] <= bag:
        heapq.heappush(heap, -jewels[idx][1])
        idx += 1

    if heap:
        result += -heapq.heappop(heap)

print(result)