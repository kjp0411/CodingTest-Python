# https://www.acmicpc.net/problem/10989
# 코드1 (메모리 초과)
# N = int(input())
# A = [0] * N
# for i in range(N):
#     A[i] = int(input())
#
# A = sorted(A)
#
# for i in range(N):
#     print(A[i])

# 코드2 메모리: 33432KB 시간: 7968ms
import sys
input = sys.stdin.readline

N = int(input())
count = [0] * 10001

for i in range(N):
    count[int(input())] += 1

for i in range(10001):
    if count[i] != 0:
        for _ in range(count[i]):
            print(i)