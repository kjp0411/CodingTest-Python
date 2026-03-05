# https://www.acmicpc.net/problem/24337
N, A, B = map(int, input().split())

# 물리적으로 불가능한 경우: A + B - 1 > N
if A + B - 1 > N:
    print(-1)
    exit()

# 기본 구조 1 2 ... (A-1) | MAX | (B-1) ... 2 1
MAX = max(A, B)

# 남는 건물
extra = N - (A + B -1)

result = []

for i in range(1, A):
    result.append(i)

result.append(MAX)

for j in range(B-1, 0, -1):
    result.append(j)

if A > 1:
    result = [1] * extra + result
elif A == 1:
    result = [result[0]] + [1] * extra + result[1:]

print(*result)