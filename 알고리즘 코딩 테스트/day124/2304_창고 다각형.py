# https://www.acmicpc.net/problem/2304
import sys
input = sys.stdin.readline

N = int(input())
bars = []
for _ in range(N):
    L, H = map(int, input().strip().split())
    bars.append((L, H))
sorted_bars = sorted(bars)

# 최고 기둥 기준 분리
max_index = 0
max_height = 0
for i, j in enumerate(sorted_bars):
    if sorted_bars[i][1] > max_height:
        max_height = sorted_bars[i][1]
        max_index = i

# 왼쪽 구간
area = 0
cur_max_height = 0
for k in range(max_index):
    if sorted_bars[k][1] > cur_max_height:
        cur_max_height = sorted_bars[k][1]
    area += (sorted_bars[k+1][0] - sorted_bars[k][0]) * cur_max_height

# 오른쪽 구간
cur_max_height = 0
for l in range(N-1, max_index, -1):
    if sorted_bars[l][1] > cur_max_height:
        cur_max_height = sorted_bars[l][1]
    area += (sorted_bars[l][0] - sorted_bars[l-1][0]) * cur_max_height

# 최고 기둥 포함
area += sorted_bars[max_index][1]
print(area)