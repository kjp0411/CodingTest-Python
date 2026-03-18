# https://www.acmicpc.net/problem/1911
import sys

input = sys.stdin.readline

N, L = map(int, input().split())

pools = []
for _ in range(N):
    S, E = map(int, input().split())
    pools.append((S, E))

pools.sort()

pos = 0
result = 0

for s, e in pools:

    # 이미 이전 널빤지로 덮은 위치(pos)가
    # 현재 웅덩이 시작점(s)보다 뒤라면
    # 실제로 덮어야 할 시작 위치는 pos부터가 된다
    if pos > s:
        s = pos

    # 시작점이 끝점보다 크거나 같다면
    # 이 웅덩이는 이미 전부 덮여있는 상태이므로
    # 널빤지를 추가로 놓을 필요가 없다
    if s >= e:
        continue

    length = e - s
    cnt = (length + L - 1) // L

    result += cnt
    pos = s + cnt * L

print(result)