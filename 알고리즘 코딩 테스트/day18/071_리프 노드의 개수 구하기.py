# https://www.acmicpc.net/problem/1068
import sys
sys.setrecursionlimit(10**6)    # 재귀 함수를 위해 충분히 큰 수로 한곗값 설정
input = sys.stdin.readline

N = int(input())
visited = [False] * (N)
tree = [[] for _ in range(N)]
answer = 0
p = list(map(int, input().split()))

for i in range(N):
    if p[i] != -1:
        tree[i].append(p[i])
        tree[p[i]].append(i)
    else:
        root = i

# DFS 탐색 함수
def DFS(number):
    global answer
    visited[number] = True
    cNode = 0
    for i in tree[number]:
        if not visited[i] and i != deleteNode:  # 삭제 노드면 탐색 중지
            cNode += 1
            DFS(i)
    if cNode == 0:
        answer += 1 # 자식 노드 수가 0개일 때 리프 노드로 간주하고 정답 값 증가

deleteNode = int(input())

if deleteNode == root:
    print(0)
else:
    DFS(root)
    print(answer)