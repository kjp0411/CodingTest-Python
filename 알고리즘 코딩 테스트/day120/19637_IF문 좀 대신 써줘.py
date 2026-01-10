# https://www.acmicpc.net/problem/19637
import sys
from bisect import bisect_left
input = sys.stdin.readline

N, M = map(int, input().split())
titles = []
powers = []

for _ in range(N):
    name, limit = input().split()
    titles.append(name)
    powers.append(int(limit))

for _ in range(M):
    power = int(input())
    idx = bisect_left(powers, power)
    print(titles[idx])