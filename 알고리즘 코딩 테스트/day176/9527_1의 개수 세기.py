# https://www.acmicpc.net/problem/9527
A, B = map(int, input().split())

def f(n):
    if n < 0:
        return 0

    result = 0

    for k in range(60):
        block = 1 << (k+1)
        ones = 1 << k

        full_block = (n+1) // block
        result += full_block * ones

        remainder = (n+1) % block
        result += max(0, remainder - ones)

    return result

print(f(B) - f(A-1))