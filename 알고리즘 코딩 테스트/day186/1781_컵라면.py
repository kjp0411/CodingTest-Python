# https://www.acmicpc.net/problem/1781
import heapq
import sys

input = sys.stdin.readline

N = int(input())

deadlines_ramens = []

for _ in range(N):
    D, R = map(int, input().split())
    deadlines_ramens.append((D, R))

deadlines_ramens.sort()

heap = []

for d, r in deadlines_ramens:

    heapq.heappush(heap, r)

    if len(heap) > d:
        heapq.heappop(heap)

print(sum(heap))