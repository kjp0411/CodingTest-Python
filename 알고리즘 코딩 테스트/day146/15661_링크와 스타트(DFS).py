# https://www.acmicpc.net/problem/15661
N = int(input().strip())
board = [list(map(int, input().split())) for _ in range(N)]

selected = [False] * N
ans = float('inf')

def dfs(idx, cnt, start_score, link_score):
    global ans

    # 사람은 다 봤을 때만 점수 계산
    if idx == N:
        if cnt == 0 or cnt == N: return
        ans = min(ans, abs(start_score - link_score))
        return

    selected[idx] = True
    start, link = 0, 0

    # idx번 사람을 팀 A에 넣는 경우
    for j in range(idx):
        if selected[j] == True:
            start += board[idx][j] + board[j][idx]
    dfs(idx + 1, cnt + 1, start_score + start, link_score)
    selected[idx] = False

    # idx번 사람을 팀 B에 두는 경우
    for j in range(idx):
        if selected[j] == False:
            link += board[idx][j] + board[j][idx]
    dfs(idx + 1, cnt, start_score, link_score + link)
    selected[idx] = False

selected[0] = True
dfs(1,1, 0, 0)
print(ans)