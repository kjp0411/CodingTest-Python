# https://www.acmicpc.net/problem/2668
N = int(input())
table = [0] # 0번은 더미(사용 X)

for _ in range(N):
    table.append(int(input()))

visited = [False] * (N+1)     # 전체 방문 체크
finished = [False] * (N+1)    # 해당 노드의 DFS 탐색이 완전히 종료되었는지 여부
result = []

def dfs(x):
    visited[x] = True
    next = table[x]

    if not visited[next]:
        dfs(next)
    elif not finished[next]:
        # 사이클 발견
        cur = next
        while True:
            result.append(cur)
            cur = table[cur]
            if cur == next:
                break
    finished[x] = True

# 모든 노드 DFS
for i in range(1, N+1):
    if not visited[i]:
        dfs(i)

# 결과 출력
result = sorted(result)
print(len(result))
for num in result:
    print(num)