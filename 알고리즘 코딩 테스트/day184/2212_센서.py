# https://www.acmicpc.net/problem/2212
N = int(input())
K = int(input())
sensors = sorted(map(int, input().split()))

diff = []

for i in range(1, N):
    diff.append(sensors[i] - sensors[i-1])

diff.sort()
print(sum(diff[:N-K]))