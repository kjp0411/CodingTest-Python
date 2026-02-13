# https://www.acmicpc.net/problem/15989
import sys
input = sys.stdin.readline

T = int(input())
nums = [int(input()) for _ in range(T)]

max_n = max(nums)

dp = [0] * (max_n + 1)
dp[0] = 1   # 0을 만드는 방법은 1가지


for selected in [1,2,3]:
    for i in range(selected, max_n + 1):
        dp[i] += dp[i - selected]

for n in nums:
    print(dp[n])