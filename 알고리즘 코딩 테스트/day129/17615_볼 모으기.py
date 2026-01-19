# https://www.acmicpc.net/problem/17615
N = int(input())
a = input()

red = a.count('R')
blue = N - red
ans = min(red, blue)
cnt = 0

for i in range(N):
    if a[i] != a[0]:
        break
    cnt += 1
if a[0] == 'R':
    ans = min(ans, red - cnt)
else:
    ans = min(ans, blue - cnt)

cnt = 0
for i in range(N-1, -1, -1):
    if a[i] != a[N - 1]:
        break
    cnt += 1
if a[N - 1] == 'R':
    ans = min(ans, red - cnt)
else:
    ans = min(ans, blue - cnt)
print(ans)
