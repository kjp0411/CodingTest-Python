# https://www.acmicpc.net/problem/21568
A, B, C = map(int, input().split())

def gcd(A, B):
    if B == 0:
        return A
    else:
        return gcd(B, A % B)

def Execute(A, B):
    ret = [0] * 2
    if B == 0:
        ret[0] = 1
        ret[1] = 0
        return ret
    q = A // B
    v = Execute(B, A % B)   # 재귀 형태로 유클리드 호제법 수행
    ret[0] = v[1]           # 역순으로 올라오면서 x, y를 계산하는 로직
    ret[1] = v[0] - v[1] * q
    return ret

mgcd = gcd(A, B)

if C % mgcd != 0:
    print(-1)
else:
    mok = int(C / mgcd)
    ret = Execute(A, B)
    print(ret[0] * mok, end=' ')
    print(ret[1] * mok)