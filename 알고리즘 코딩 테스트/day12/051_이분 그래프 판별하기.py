# https://www.acmicpc.net/problem/1707
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
IsEven = True

def DFS(node):
    global IsEven
    visited[node] = True
    for i in A[node]:
        if not visited[i]:
            # 인접 노드는 같은 집합이 아니므로 다른 집합으로 처리
            check[i] = (check[node]+1)%2
            DFS(i)
        # 이미 방문한 노드가 현재 내 노드와 같은 집합이면 이분 그래프 아님
        elif check[node] == check[i]:
            IsEven = False


for _ in range(N):
    V, E = map(int, input().split())
    A = [[] for _ in range(V + 1)]
    visited = [False] * (V + 1)
    check = [0] * (V + 1)
    IsEven = True
    for i in range(E):  # 인접 리스트로 그래프 저장
        Start, End = map(int, input().split())
        A[Start].append(End)
        A[End].append(Start)

    # 주어진 그래프가 항상 1개가 아니므로 모든 노드에서 수행
    for i in range(1, V + 1):
        if IsEven:
            DFS(i)
        else:
            break

    if IsEven:
        print("YES")
    else:
        print("NO")