# https://www.acmicpc.net/problem/11726
N = int(input())
D = [0] * (1001)
D[1] = 1
D[2] = 2

for i in range(3, N + 1):
    D[i] = (D[i - 1] + D[i - 2]) % 10007

print(D[N])