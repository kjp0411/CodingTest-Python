# https://www.acmicpc.net/problem/11501
# 매일 그는 아래 세 가지 중 한 행동을 한다.
# 1. 주식 하나를 산다.
# 2. 원하는 만큼 가지고 있는 주식을 판다.
# 3. 아무것도 안한다.
import sys
input = sys.stdin.readline

T = int(input().strip())
for _ in range(T):
    purchase = 0
    day = int(input().strip())
    stock = list(map(int, input().strip().split()))
    max_stock = 0
    for i in range(day, 0, -1):
        if stock[i-1] > max_stock:
            max_stock = stock[i-1]
        else:   # 최댓값보다 작다면
            purchase += max_stock - stock[i-1]
    print(purchase)