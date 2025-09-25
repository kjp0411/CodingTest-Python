# https://www.acmicpc.net/problem/1219
import sys
input = sys.stdin.readline

N, sDosi, eDosi, M = map(int, input().split())
edges = []
distance = [-sys.maxsize] * N   # 최딘거리 리스트 초기화

for _ in range(M):  # 엣지 데이터 저장
    s, e, p = map(int, input().split())
    edges.append((s, e, p))

dosiMoney = list(map(int, input().split()))

# 변형된 벨만 포드 수행
distance[sDosi] = dosiMoney[sDosi]  # 출발 초기화

for i in range(N + 101):
    for s, e, p in edges:
        if distance[s] == -sys.maxsize:
                continue
        elif distance[s] == sys.maxsize:
            distance[e] = sys.maxsize
        # 더 많은 돈을 벌 수 있는 새로운 경로가 있는 경우 값 업데이트
        elif distance[e] < distance[s] + dosiMoney[e] - p:
            distance[e] = distance[s] + dosiMoney[e] - p
            if i >= N - 1:
                distance[e] = sys.maxsize

if distance[eDosi] == -sys.maxsize:     # 도착 불가능
    print('gg')
elif distance[eDosi] == sys.maxsize:    # 양수 사이클 -> 무한대로 돈을 벌 수 있을 경우
    print('Gee')
else:
    print(distance[eDosi])