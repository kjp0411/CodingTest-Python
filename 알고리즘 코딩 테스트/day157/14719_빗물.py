# https://www.acmicpc.net/problem/14719
import sys
input = sys.stdin.readline

H, W = map(int, input().split())
height = list(map(int, input().split()))

left = 0
right = W-1
left_max = 0
right_max = 0
answer = 0

while left < right: # l은 늘리고 r은 줄이면서 서로 넘어가면 종료(W == 1인 경우 탐색 X)
    left_max = max(left_max, height[left])
    right_max = max(right_max, height[right])

    if left_max < right_max:
        answer += left_max - height[left]
        left += 1
    else:
        answer += right_max - height[right]
        right -= 1

print(answer)