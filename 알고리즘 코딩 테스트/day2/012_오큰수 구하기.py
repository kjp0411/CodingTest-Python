# https://www.acmicpc.net/problem/17298
import sys
input = sys.stdin.readline

N = int(input())
answer = [0] * N
A = list(map(int, input().split()))
stack = []

for i in range(N):
    # 스택이 비어 있지 않고 현재 수열이 스택 top 인덱스가 가리키는 수열보다 클 경우
    while stack and A[stack[-1]] < A[i]:
        answer[stack.pop()] = A[i]
    stack.append(i)

while stack:
    answer[stack.pop()] = -1

for i in range(N):
    print(answer[i], end= " ")