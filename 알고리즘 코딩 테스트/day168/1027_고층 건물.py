# https://www.acmicpc.net/problem/1027
import sys
input = sys.stdin.readline

N = int(input())
building_h = list(map(int, input().split()))
answer = 0

for i in range(N):
    count = 0

    for j in range(N):
        if i == j:
            continue

        visible = True
        dx = abs(j - i)

        for k in range(min(i, j) + 1, max(i, j)):
            if (building_h[k] - building_h[i]) * dx >= (building_h[j] - building_h[i]) * abs(k - i):
                visible = False
                break

        if visible:
            count += 1

    answer = max(answer, count)

print(answer)