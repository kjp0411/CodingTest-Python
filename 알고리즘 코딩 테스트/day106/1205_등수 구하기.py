# https://www.acmicpc.net/problem/1205
import sys
input = sys.stdin.readline

N, new_score, P = map(int, input().split())

if N == 0:
    print(1)
    exit()

scores = list(map(int, input().split()))

if N == P and new_score <= scores[-1]:
    print(-1)
    exit()

rank = 1
for s in scores:
    if new_score < s:
        rank += 1
    else:
        break

print(rank)