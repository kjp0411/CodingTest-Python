# https://www.acmicpc.net/problem/1806
N, S = map(int, input().split())
A = list(map(int, input().split()))

left = 0
right = 0
sum_value = 0
min_length = 10**9

while right <= N:
    if sum_value >= S and left < N:
        min_length = min(min_length, (right - left))
        sum_value -= A[left]
        left += 1
    elif sum_value < S and right < N:
        sum_value += A[right]
        right += 1
    elif sum_value < S and right == N:
        break

if min_length == 10**9:
    print(0)
else:
    print(min_length)