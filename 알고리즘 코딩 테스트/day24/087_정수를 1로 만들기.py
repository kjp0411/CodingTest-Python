# https://www.acmicpc.net/problem/1463
N = int(input())
D = [0] * (N + 1)
D[1] = 0    # 1일 때는 연산 불필요

for i in range(2, N + 1):
    D[i] = D[i - 1] + 1                     # 1을 빼는 연산
    if i % 2 == 0:
        D[i] = min(D[i], D[i // 2] + 1)     # 나누기 2 연산
    if i % 3 == 0:
        D[i] = min(D[i], D[i // 3] + 1)     # 나누기 3 연산

print(D[N])