# https://www.acmicpc.net/problem/7490
T = int(input())

def dfs(num, expr):
    if num == N:
        if calculate(expr) == 0:
            print(expr)
        return

    next_num = num + 1

    dfs(next_num, expr + " " + str(next_num))
    dfs(next_num, expr + "+" + str(next_num))
    dfs(next_num, expr + "-" + str(next_num))

def calculate(expr):
    expr = expr.replace(" ", "")
    total = 0
    num = 0
    sign = 1

    for ch in expr:
        if ch.isdigit():
            num = num * 10 + int(ch)
        else:
            total += sign * num
            num = 0
            if ch == '+':
                sign = 1
            else:
                sign = -1

    total += sign * num
    return total

for t in range(T):
    N = int(input())
    dfs(1, "1")

    if t != T-1:
        print()