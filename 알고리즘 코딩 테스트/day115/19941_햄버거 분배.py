# https://www.acmicpc.net/problem/19941
N, K = map(int, input().split())
table = list(input())
for i in range(N):
    if table[i] == 'P':
        for j in range(max(0, i-K), min(N, i+K+1)):
            if table[j] == 'H':
                table[j] = 'E'  # 먹었다고 표시
                break
print(table.count('E'))