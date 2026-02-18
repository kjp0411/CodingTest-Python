# https://www.acmicpc.net/problem/2467
N = int(input())
liquids = list(map(int, input().split()))

left = 0
right = N-1
min_s = 10**18
ans = (0, 0)

while left < right:     # left가 right보다 작을 때만 진행
    raw_sum = liquids[left] + liquids[right]
    s = abs(raw_sum)

    if s < min_s:
        min_s = s
        ans = (liquids[left], liquids[right])

    if raw_sum > 0:
        right -= 1
    elif raw_sum < 0:
        left += 1
    else:
        break

print(ans[0], ans[1])