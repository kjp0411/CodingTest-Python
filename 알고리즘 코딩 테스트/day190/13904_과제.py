# https://www.acmicpc.net/problem/13904
import heapq
import sys

input = sys.stdin.readline

N = int(input())

tasks = []

for _ in range(N):
    D, W = map(int, input().split())
    tasks.append((D, W))

tasks.sort()

heap = []

for d, w in tasks:
    heapq.heappush(heap, w)

    if len(heap) > d:
        heapq.heappop(heap)

print(sum(heap))