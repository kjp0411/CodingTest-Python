# https://www.acmicpc.net/problem/17298
import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
NGE = []
answer = [0] * N

for i in range(N):
    while NGE and A[NGE[-1]] < A[i]:
        answer[NGE.pop()] = A[i]
    NGE.append(i)

while NGE:
    answer[NGE.pop()] = -1

print(*answer)