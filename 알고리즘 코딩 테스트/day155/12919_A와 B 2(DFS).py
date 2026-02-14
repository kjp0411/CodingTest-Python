# https://www.acmicpc.net/problem/12919
S = input().strip()
T = input().strip()
found = False
def dfs(cur):
    global found

    # 종료 조건
    if found:
        return

    if len(cur) < len(S):
        return

    if len(cur) == len(S):
        if cur == S:
            found = True
        return

    if len(cur) > len(S):
        if cur[-1] == 'A':
            dfs(cur[:-1])

        if cur[0] == 'B':
            dfs(cur[1:][::-1])

dfs(T)

if found:
    print(1)
else:
    print(0)