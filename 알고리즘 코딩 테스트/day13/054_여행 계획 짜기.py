# https://www.acmicpc.net/problem/1976
N = int(input())
M = int(input())
dosi = [[0 for j in range(N+1)] for i in range(N + 1)]

def find(a):        # find 연산
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]

def union(a, b):    # union 연산: 대표 노드끼리 연결하기
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a

for i in range(1, N + 1):   # 도시 연결 데이터 저장
    dosi[i] = list(map(int, input().split()))
    dosi[i].insert(0, 0)

route = list(map(int, input().split()))     # 여행 도시 정보 저장
route.insert(0, 0)

parent = [0] * (N + 1)

for i in range(1, N + 1):   # 대표 노드를 자기 자신으로 초기화
    parent[i] = i

for i in range(1, N + 1):   # 인접 행렬에서 도시가 연결되어 있으면 union 실행
    for j in range(1, N + 1):
        if dosi[i][j] == 1:
            union(i, j)

index = find(route[1])
isConnect = True
for i in range(2, len(route)):
    if index != find(route[i]):
        isConnect =False
        break

if isConnect:
    print("YES")
else:
    print("NO")