# https://www.acmicpc.net/problem/15684
# 사다리 게임은 N개의 세로선과 M개의 가로선으로 이루어져있다.
# 사다리에 가로선을 추가해서, 사다리 게임의 결과를 조작하려고 한다.
# 이때, i번 세로선의 결과가 i번이 나와야 한다.
# 그렇게 하기 위해서 추가해야 하는 가로선 개수의 최솟값을 구하시오.
# Python 3 시간 초과 -> PyPy3 통과
import sys
input = sys.stdin.readline

N, M, H = map(int, input().split())
ladder = [[False] * (N+1) for _ in range(H+1)]

for _ in range(M):
    a, b = map(int, input().split())  # a층에서 b와 b+1 연결
    ladder[a][b] = True

def simulate():
    """사다리 결과 확인"""
    for start in range(1, N+1):
        pos = start
        for h in range(1, H+1):
            if ladder[h][pos]:                  # 오른쪽으로 이동
                pos += 1
            elif pos > 1 and ladder[h][pos-1]:  # 왼쪽으로 이동
                pos -= 1

        if pos != start:
            return False
    return True


answer = 4  # 0~3 가능, 4는 불가능 표시

def dfs(cnt, row, target):
    global answer

    if cnt == target:
        if simulate():
            answer = target
        return

    # 가지치기: 이미 더 좋은 해가 나오면 중단
    if answer != 4:
        return

    for h in range(row, H+1):
        for n in range(1, N):
            if ladder[h][n] or ladder[h][n-1] or ladder[h][n+1]:
                continue

            ladder[h][n] = True
            dfs(cnt+1, h, target)
            ladder[h][n] = False

            if answer != 4:   # 이미 해가 나왔으면 더 볼 필요 없음
                return


for target in range(4):
    dfs(0, 1, target)
    if answer != 4:
        break

print(answer if answer < 4 else -1)
