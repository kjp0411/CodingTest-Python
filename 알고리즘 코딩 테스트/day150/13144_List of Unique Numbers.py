# https://www.acmicpc.net/problem/13144
N = int(input())
A = list(map(int, input().split()))

l = 0
cnt = {}
ans = 0

for r in range(N):
    cnt[A[r]] = cnt.get(A[r], 0) + 1

    while cnt[A[r]] > 1:
        cnt[A[l]] -= 1
        l += 1
    ans += r - l + 1

print(ans)