# https://www.acmicpc.net/problem/1092
import sys

input = sys.stdin.readline

N = int(input())
weight_limits = list(map(int, input().split()))
M = int(input())
weight_boxs = list(map(int, input().split()))

weight_limits.sort(reverse=True)
weight_boxs.sort(reverse=True)

# 만약 모든 박스를 배로 옮길 수 없으면 -1을 출력한다.
if weight_boxs[0] > weight_limits[0]:
    print(-1)
    sys.exit()

positions = [0] * N      # 각 크레인이 현재 보고 있는 박스 위치
checked = [False] * M    # 옮긴 박스인지 표시
count = 0                # 옮긴 박스 수
time = 0

while count < M:
    for i in range(N):
        while positions[i] < M:
            if not checked[positions[i]] and weight_limits[i] >= weight_boxs[positions[i]]:
                checked[positions[i]] = True
                positions[i] += 1
                count += 1
                break
            positions[i] += 1
    time += 1

print(time)