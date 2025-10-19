# https://www.acmicpc.net/problem/2098
# 도시에는 1번부터 N번까지 번호가 매겨져 있음
# 도시 사이에는 길이 있을 수도 있고 없을 수도 있음
# 한 도시에서 출발해 N개의 도시를 모두 거쳐 다시 원래 도시로 돌아와야 됨
# 단, 한 번 갔던 도시는 다시 갈 수 없음(마지막에 돌아오는 건 가능)
# 가장 적은 비용이 드는 여행 계획을 구해야 됨
# W[i][j]: 각 도시(도시 i에서 도시 j로)간에 이동하는데 드는 비용
# 비용은 대칭적이지 않다.(W[i][j] != W[j][i])
# 비용은 양의 정수
# W[i][i]: 항상 0
# 도시 i에서 도시 j로 갈 수 없는 경우 W[i][j] = 0으로 표기

N = int(input())
W = []

for i in range(N):
    W.append([])
    W[i] = list(map(int, input().split()))

D = [[0 for j in range(1 << 16)] for i in range(16)]

def TSP(c, v):
    if v == (1 << N) - 1:
        if W[c][0] == 0:
            return float('inf')
        else:
            return W[c][0]

    if D[c][v] != 0:
        return D[c][v]
    min_value = float('inf')
    for i in range(0, N):
        if (v & (1 << i)) == 0 and W[c][i] != 0:
            min_value = min(min_value, TSP(i, (v | (1 << i))) + W[c][i])
    D[c][v] = min_value
    return D[c][v]

print(TSP(0, 1))