# https://www.acmicpc.net/problem/20922
import sys
input = sys.stdin.readline

N, K = map(int, input().strip().split())
A = list(map(int, input().strip().split()))
l = 0                      # 왼쪽 포인터
count = {}                 # 현재 구간 상태 저장용
answer = 0

for r in range(N):         # 오른쪽 포인터
    x = A[r]
    # 1. 오른쪽 원소 처리
    if x in count:
        count[x] = count[x] + 1
    else:
        count[x] = 1

    # 2. 조건이 깨졌다면 왼쪽 포인터 이동
    while count[x] > K:
        y = A[l]
        count[y] = count[y] - 1
        l += 1

    # 3. 조건을 만족하는 상태에서 정답 갱신
    if answer < (r - l + 1):
        answer = r - l + 1

print(answer)