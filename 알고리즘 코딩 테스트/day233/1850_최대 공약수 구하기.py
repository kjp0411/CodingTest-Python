# https://www.acmicpc.net/problem/1850
def gcd(A, B):
    if B == 0:
        return A
    else:
        return gcd(B, A % B)    # 재귀 함수 형태로 구현

A, B = map(int, input().split())
result = gcd(A, B)

while result > 0:
    print(1, end='')
    result -= 1