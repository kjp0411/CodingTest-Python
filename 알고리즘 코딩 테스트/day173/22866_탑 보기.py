# https://www.acmicpc.net/problem/22866
import sys
input = sys.stdin.readline

N = int(input())
heights = list(map(int, input().split()))

visible = [0] * N
nearest = [-1] * N

# 왼쪽
stack = [] # index 저장
for i in range(N):
    while stack and heights[stack[-1]] <= heights[i]:
        stack.pop()
    visible[i] += len(stack)
    if stack:
        nearest[i] = stack[-1]

    stack.append(i)

# 오른쪽
stack = [] # index 저장
for j in range(N-1, -1, -1):
    while stack and heights[stack[-1]] <= heights[j]:
        stack.pop()  # 마지막 값이 제거

    visible[j] += len(stack)

    left = nearest[j]
    if stack:
        right = stack[-1]

        if left == -1:
            nearest[j] = right
        else:
            dist_left = j - left
            dist_right = right - j

            if dist_left < dist_right:
                pass
            elif dist_left > dist_right:
                nearest[j] = right
            else:
                nearest[j] = min(nearest[j], right)

    stack.append(j)

for k in range(N):
    if visible[k] == 0:
        print(0)
    else:
        print(visible[k], nearest[k] + 1)