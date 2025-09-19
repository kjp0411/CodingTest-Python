# https://www.acmicpc.net/problem/15649
N, M = map(int, input().split())
S = [0] * M                     # 수열을 저장할 리스트
visited = [False] * N           # 숫자 사용 여부 저장 리스트

def backtrack(length):
    if length == M:             # 길이가 M인 수열이 만들어진 경우
        print(' '.join(str(x + 1) for x in S))
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            S[length] = i
            backtrack(length + 1)
            visited[i] = False  # 백트래킹(수 반납)

backtrack(0)