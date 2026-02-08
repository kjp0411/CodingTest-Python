# https://www.acmicpc.net/problem/16472
N = int(input())
S = input().strip()

l = 0
cnt = {}
kind = 0
ans = 0

for r in range(len(S)):
    if cnt.get(S[r], 0) == 0:
        kind += 1
    cnt[S[r]] = cnt.get(S[r], 0) + 1

    while kind > N: # 종류가 N을 넘어가면 l을 증가시키면서 kind 줄여야함
        cnt[S[l]] -= 1
        if cnt[S[l]] == 0:
            kind -= 1
        l += 1
    ans = max(ans, r - l + 1)
print(ans)