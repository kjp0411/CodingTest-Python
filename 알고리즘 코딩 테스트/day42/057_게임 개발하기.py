# https://www.acmicpc.net/problem/1516
from collections import deque
N = int(input())
A = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)    # 진입 차수 리스트
selfBuild = [0] * (N + 1)   # 자기 자신을 짓는 데 걸리는 시간

for i in range(1, N + 1):
    inputList = list(map(int, input().split()))
    selfBuild[i] = (inputList[0])   # 해당 건물을 짓는데 걸리는 시간
    index = 1
    while True:     # 인접 리스트 만들기
        preTemp = inputList[index]
        index += 1
        if preTemp == -1:
            break
        A[preTemp].append(i)
        indegree[i] += 1    # 진입 차수 데이터 저장

queue = deque()

for i in range(1, N + 1):
    if indegree[i] == 0:
        queue.append(i)

result = [0] * (N + 1)

while queue:    # 위상 정렬 수행
    now = queue.popleft()
    for next in A[now]:
        indegree[next] -= 1
        # 시간 업데이트
        result[next] = max(result[next], result[now] + selfBuild[now])
        if indegree[next] == 0:
            queue.append(next)

for i in range(1, N + 1):
    print(result[i] + selfBuild[i])