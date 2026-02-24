# https://www.acmicpc.net/problem/1863
N = int(input())
building_h = []

for _ in range(N):
    x, y = map(int, input().split())
    building_h.append(y)

stack = []
count = 0

for h in building_h:
    while stack and stack[-1] > h:
        stack.pop()
        count += 1

    if h > 0 and (not stack or stack[-1] < h):
        stack.append(h)

count += len(stack)
print(count)