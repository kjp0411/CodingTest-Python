# https://www.acmicpc.net/problem/14888
N = int(input())
A = list(map(int, input().split()))
ops = list(map(int, input().split()))

max_value = -1e18
min_value = 1e18

def calc(a, b, op):
    if op == 0:
        return a + b
    elif op == 1:
        return a - b
    elif op == 2:
        return a * b
    else:
        if a < 0:
            return -(-a // b)
        else:
            return a // b

def dfs(idx, current):
    global max_value, min_value

    if idx == N:
        max_value = max(max_value, current)
        min_value = min(min_value, current)
        return

    for i in range(4):
        if ops[i] > 0:
            ops[i] -= 1
            dfs(idx + 1, calc(current, A[idx], i))
            ops[i] += 1

dfs(1, A[0])

print(max_value)
print(min_value)