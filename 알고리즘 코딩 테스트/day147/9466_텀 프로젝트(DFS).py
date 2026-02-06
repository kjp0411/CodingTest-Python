# https://www.acmicpc.net/problem/9466
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    S = [0] + list(map(int, input().split()))

    visited = [False] * (N + 1)
    finished = [False] * (N + 1)
    cnt = [0]
    def dfs(x):
        visited[x] = True
        next = S[x]

        if not visited[next]:
            dfs(next)
        else:
            if not finished[next]:
                cur = next
                cnt[0] += 1
                cur = S[cur]
                while cur != next:
                    cnt[0] += 1
                    cur = S[cur]

        finished[x] = True

    for i in range(1, N + 1):
        if not visited[i]:
            dfs(i)

    print(N - cnt[0])