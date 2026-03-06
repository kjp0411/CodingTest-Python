# https://www.acmicpc.net/problem/1943
# # 코드1 (시간 초과)
# import sys
# input = sys.stdin.readline
#
# for _ in range(3):
#     N = int(input())    # 동전의 종류
#     coins = []
#     total = 0
#     for _ in range(N):
#         coin_value, coin_count = map(int, input().split())
#         total += coin_value * coin_count
#         coins.append((coin_value, coin_count))
#
#     # 불가능한 경우
#     if total % 2 == 1:
#         print(0)
#         continue
#
#     # 가능해 보이는 경우(한번더 판단)
#     target = total // 2
#
#     dp = [False] * (target + 1)
#     dp[0] = True
#
#     for value, count in coins:
#         for _ in range(count):
#             for i in range(target, value-1, -1):
#                 if dp[i-value]:
#                     dp[i] = True
#
#     if dp[target]:
#         print(1)
#     else:
#         print(0)

# 코드2 (이진 분할)
import sys
input = sys.stdin.readline

for _ in range(3):
    N = int(input())    # 동전의 종류
    coins = []
    total = 0
    for _ in range(N):
        coin_value, coin_count = map(int, input().split())
        total += coin_value * coin_count
        coins.append((coin_value, coin_count))

    # 불가능한 경우
    if total % 2 == 1:
        print(0)
        continue

    # 가능해 보이는 경우(한번더 판단)
    target = total // 2

    dp = [False] * (target + 1)
    dp[0] = True

    for value, count in coins:
        k = 1
        while count > 0:
            use = min(k, count)
            weight = value * use

            for i in range(target, weight-1, -1):
                if dp[i-weight]:
                    dp[i] = True

            count -= use
            k *= 2

    if dp[target]:
        print(1)
    else:
        print(0)