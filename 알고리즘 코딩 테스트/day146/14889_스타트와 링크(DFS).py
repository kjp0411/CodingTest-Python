# https://www.acmicpc.net/problem/14889
N = int(input().strip())
board = [list(map(int, input().split())) for _ in range(N)]

selected = [False] * N
ans = float('inf')
def dfs(idx, cnt):
    global ans

    # 팀 A가 정확히 N//2명일 때만 점수 계산
    if cnt == N//2:
        start, link = 0, 0
        for i in range(N):
            for j in range(N):
                if selected[i] and selected[j]:
                    start += board[i][j]
                elif not selected[i] and not selected[j]:
                    link += board[i][j]
        ans = min(ans, abs(start - link))
        return

    # 사람은 다 봤는데 팀A가 N//2 안 된 경우
    if idx == N:
        return

    # 가지치기: 남은 사람으로 팀을 채울 수 없는 경우
    if cnt + (N - idx) < N // 2:
        return

    # idx번 사람을 팀 A에 넣는 경우
    selected[idx] = True
    dfs(idx + 1, cnt + 1)

    # idx번 사람을 팀 B에 두는 경우
    selected[idx] = False
    dfs(idx + 1, cnt)

# 대칭 제거: 0번 사람을 무조건 팀 A에 넣고 시작
selected[0] = True
dfs(1,1)
print(ans)