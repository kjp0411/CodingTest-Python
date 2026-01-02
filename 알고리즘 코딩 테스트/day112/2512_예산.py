# https://www.acmicpc.net/problem/2512
# 국가예산의 총액은 미리 정해져 있어서 모든 예산요청을 배정해 주지 못할 수도 있음
# (정해진 총액 이하에서 가능한 최대의 총 예산을 배정한다.)
# 1. 모든 요청이 배정될 수 있는 경우에는 요청한 금액을 그대로 배정한다.
# 2. 모든 요청이 배정될 수 없는 경우에는 특정한 정수 상한액을 계산하여 그 이상인 예산요청에는 모두 상한액을 배정한다.
# 상한액 이하의 예산요청에 대해서는 요청한 금액을 그대로 배정한다.

import sys
input = sys.stdin.readline

N = int(input())
budgets = list(map(int, input().split()))
M = int(input())

# cap 판별 함수
cap = 0
def valid(cap):
    total = 0
    for b in budgets:
        total += min(b, cap)
    if total <= M:
        return True
    else:
        return False

# 전부 배정 가능한 경우
if sum(budgets) <= M:
    print(max(budgets))
    sys.exit()

# cap 범위 잡기
left = 0
right = max(budgets)
answer = 0

# 이분 탐색으로 최대 cap 찾기
while left <= right:
    mid = (left + right) // 2

    if valid(mid):
        answer = mid        # 가능한 ca 저장
        left = mid + 1      # 더 큰 cap 시도
    else:
        right = mid - 1     # mid 이상 전부 컷

print(answer)