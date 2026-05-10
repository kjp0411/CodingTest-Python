# https://www.acmicpc.net/problem/1934
def gcd(A, B):
    if B == 0:
        return A
    else:
        return gcd(B, A % B)    # 재귀 함수 형태로 구현

T = int(input())

for i in range(T):
    A, B = map(int, input().split())
    result = A * B / gcd(A, B)
    print(int(result))