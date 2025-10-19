# https://www.acmicpc.net/problem/11049
# Python 3 시간 초과 -> PyPy3 통과
import sys
input = sys.stdin.readline

N = int(input())
M = []
D = [[-1 for j in range(N + 1)] for i in range(N + 1)]

M.append((0, 0))    # 인덱스를 1부터 사용하기 위해서

for i in range(N):
    r, c = map(int, input().split())
    M.append((r, c))

def execute(s, e):  # 탑-다운 방식 점화식 함수
    result = sys.maxsize
    if D[s][e] != -1:
        return D[s][e]
    if s == e:
        return 0
    if s + 1 == e:
        return M[s][0] * M[s][1] * M[e][1]
    for i in range(s, e):
        result = min(result, M[s][0] * M[i][1] * M[e][1] + execute(s, i) + execute(i + 1, e))
    D[s][e] = result
    return D[s][e]

print(execute(1, N))