# https://www.acmicpc.net/problem/11000
import heapq
import sys

input = sys.stdin.readline

N = int(input())
studies = []

for _ in range(N):
    S, T = map(int, input().split())
    studies.append((S, T))

studies.sort()

heap = []

for s, t in studies:

    # 가장 먼저 끝나는 강의실 찾기
    if heap and heap[0] <= s:
        heapq.heappop(heap)

    # 현재 강의 종료 시간
    heapq.heappush(heap, t)

print(len(heap))