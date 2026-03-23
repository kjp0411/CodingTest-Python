# https://www.acmicpc.net/problem/11720
import sys

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().strip()))

sum_value = 0

for i in range(N):
    sum_value += nums[i]

print(sum_value)