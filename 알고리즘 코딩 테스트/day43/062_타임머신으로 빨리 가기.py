# https://www.acmicpc.net/problem/11657
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
edges = []
distance = [sys.maxsize] * (N + 1)

for i in range(M):  # 엣지 데이터 저장
    s, e, t = map(int, input().split())
    edges.append((s, e, t))

# 벨만 포드 수행
distance[1] = 0

for _ in range(N - 1):
    for s, e, t in edges:
        if distance[s] != sys.maxsize and distance[e] > distance[s] + t:
            distance[e] = distance[s] + t

# 음수 사이클 확인
mCycle = False

for s, e, t in edges:
    if distance[s] != sys.maxsize and distance[e] > distance[s] + t:
        mCycle = True

if not mCycle:
    for i in range(2, N + 1):
        if distance[i] != sys.maxsize:
            print(distance[i])
        else:
            print(-1)

else:
    print(-1)