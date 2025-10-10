# https://www.acmicpc.net/problem/2162
# Python 3 시간 초과 -> PyPy3 통과
import sys
input = sys.stdin.readline
N = int(input())
parent = [-1] * (3001)

# CCW 공식
def CCW(x1, y1, x2, y2, x3, y3):
    temp = (x1 * y2 + x2 * y3 + x3 * y1) - (x2 * y1 + x3 * y2 + x1 * y3)
    if temp > 0:
        return 1
    elif temp < 0:
        return -1
    else:
        return 0

# 선분 겹침 여부 판별 함수
def isOverlab(x1, y1, x2, y2, x3, y3, x4, y4):
    if min(x1, x2) <= max(x3, x4) and min(x3, x4) <= max(x1, x2) \
            and min(y1, y2) <= max(y3, y4) and min(y3, y4) <= max(y1, y2):
        return True
    return False

# 선분 교차 여부 판별 함수
def isCross(x1, y1, x2, y2, x3, y3, x4, y4):
    abc = CCW(x1, y1, x2, y2, x3, y3)
    abd = CCW(x1, y1, x2, y2, x4, y4)
    cda = CCW(x3, y3, x4, y4, x1, y1)
    cdb = CCW(x3, y3, x4, y4, x2, y2)
    if abc * abd == 0 and cda * cdb == 0:
        return isOverlab(x1, y1, x2, y2, x3, y3, x4, y4)
    elif abc * abd <= 0 and cda * cdb <= 0:
        return True
    return False

# 변형된 union-find
def find(a):
    if parent[a] < 0:
        return a
    parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    p = find(a)
    q = find(b)
    if p == q:
        return
    parent[p] += parent[q]
    parent[q] = p

L = []
L.append([])

for i in range(1, N + 1):
    L.append([])
    L[i] = list(map(int, input().split()))
    for j in range(1, i):
        if isCross(L[i][0], L[i][1], L[i][2], L[i][3], L[j][0], L[j][1], L[j][2], L[j][3]):
            union(i, j)

ans = 0
result = 0

for i in range(1, N + 1):
    if parent[i] < 0:
        ans += 1
        result = min(result, parent[i])

print(ans)
print(-result)