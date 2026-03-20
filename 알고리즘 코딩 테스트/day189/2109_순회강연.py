# https://www.acmicpc.net/problem/2109
import heapq
import sys

input = sys.stdin.readline

N = int(input())

lecture = []

for _ in range(N):
    P, D = map(int, input().split())
    lecture.append((D, P))
lecture.sort()

heap = []

for d, p in lecture:
    heapq.heappush(heap, p)

    if len(heap) > d:
        heapq.heappop(heap)

print(sum(heap))