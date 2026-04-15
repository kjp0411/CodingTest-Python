# https://www.acmicpc.net/problem/9663
N = int(input())
count = 0

cols = [False] * N
diag1 = [False] * (2*N)
diag2 = [False] * (2*N)

def dfs(row):
    global count
    if row == N:
        count += 1
        return

    for col in range(N):
        if not cols[col] and not diag1[row + col] and not diag2[row - col + N]:
            cols[col] = diag1[row + col] = diag2[row - col + N] = True
            dfs(row + 1)
            cols[col] = diag1[row + col] = diag2[row - col + N] = False

dfs(0)
print(count)