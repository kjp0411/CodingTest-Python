# https://www.acmicpc.net/problem/10986
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))
D = []

# 누적합 구하기
for i in range(N):
    if i == 0:
        D.append(A[i])
    else:
        D.append(A[i]+D[i-1])

# M으로 나눈 나머지 구하기
for i in range(N):
    D[i] = D[i] % M

# 나머지 개수 세기
count = [0] * M
count[0] = 1
for i in range(N):
    count[D[i]] += 1

answer = 0

# 나머지가 같은 인덱스 중 2개를 뽑는 경우의 수 더하기
for i in range(M):
    answer += count[i] * (count[i] - 1) // 2

print(answer)