# https://www.acmicpc.net/problem/17136
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# 종이 데이터 입력받기
M = [list(map(int, input().split())) for  _ in range(10)]

# 색종이 수(크기 1~5 각각 최대 5장)
S = [0, 5, 5, 5, 5, 5]
result = float('inf')

def fill(x, y, size, value):
    for i in range(y, y + size):
        for j in range(x, x + size):
            M[i][j] = value

def check(x, y, size):
    if x + size > 10 or y + size > 10:
        return False
    for i in range(y, y + size):
        for j in range(x, x + size):
            if M[i][j] != 1:
                return False
    return True

def backtrack(pos, used):
    global result
    if pos == 100:
        result = min(result, used)
        return
    if used >= result:
        return
    x, y = divmod(pos, 10)  # x:열, y:행
    if M[y][x] == 1:
        for size in range(5, 0, -1):
            if S[size] > 0 and check(x, y, size):
                S[size] -= 1
                fill(x, y, size, 0)
                backtrack(pos + 1, used + 1)
                fill(x, y, size, 1)
                S[size] += 1
    else:
        backtrack(pos + 1, used)
backtrack(0, 0)
print(result if result != float('inf') else -1)