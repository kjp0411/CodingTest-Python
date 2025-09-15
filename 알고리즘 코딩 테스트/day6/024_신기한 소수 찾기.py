# https://www.acmicpc.net/problem/2023
# # 코드1 (시간 초과)
# import sys
# sys.setrecursionlimit(10000)
# input = sys.stdin.readline
# N = int(input())
#
# def isPrime(num):
#     for i in range(2, int(num / 2 + 1)):
#         if num % i == 0:
#             return False
#     return True
#
# def DFS(number):
#     if len(str(number)) == N:
#         print(number)
#     else:
#         for i in range(1, 10):
#             if i % 2 == 0:                  # 짝수라면 더는 탐색할 필요 없음
#                 continue
#             if isPrime(number * 10 + i):    # 소수이면 자릿수 늘림
#                 DFS(number * 10 + i)
#
# # 일의 자리 소수는 2, 3, 5, 7이므로 4가지 수에서만 시작
# DFS(2)
# DFS(3)
# DFS(5)
# DFS(7)

# 코드2 메모리: 34536KB 시간: 36ms
import sys
from math import isqrt

input = sys.stdin.readline
N = int(input())

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    r = isqrt(n)
    for d in range(3, r + 1, 2):
        if n % d == 0:
            return False
    return True

res = []

# depth: 현재 자릿수
def DFS(num: int, depth: int) -> None:
    if depth == N:
        res.append(str(num))
        return
    # 다음 자릿수 후보
    if depth == 0:
        candidates = [2, 3, 5, 7]          # 1자리 시작 소수
        for c in candidates:
            DFS(c, 1)
    else:
        for add in (1, 3, 7, 9):           # 2자리 이상은 끝자리가 홀수(5 제외)
            nxt = num * 10 + add
            if is_prime(nxt):
                DFS(nxt, depth + 1)

DFS(0, 0)
print("\n".join(res))