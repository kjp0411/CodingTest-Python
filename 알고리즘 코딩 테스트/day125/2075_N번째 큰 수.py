# https://www.acmicpc.net/problem/2075
import sys
import heapq
input = sys.stdin.readline
N = int(input())
heap = []

for _ in range(N):
    row = list(map(int, input().strip().split()))
    for i in range(N):
        if len(heap) < N:
            heapq.heappush(heap, row[i])
        else:
            if row[i] > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, row[i])
            else:
                continue

print(heap[0])