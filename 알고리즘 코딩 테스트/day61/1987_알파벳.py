# https://www.acmicpc.net/problem/1987
# R*C 크기의 보드가 있고 보드의 각 칸에는 알파벳 대문자가 하나씩 적혀 있음
# 말은 1행 1열(0, 0)에 위치하고 상, 하, 좌, 우로 이동 가능
# 새로 이동한 칸에 적혀 있는 알파벳은 지금까지 지나온 모든 칸에 적혀 있던 알파벳과 달라아 햠
# 최대한 몇 칸을 지날 수 있는지 구하시오(말이 지나는 칸은 좌측 상단(1행, 1열)도 포함)
# Python 3 시간 초과 -> PyPy3 통과
import sys
sys.setrecursionlimit(1_000_000)
input = sys.stdin.readline

R, C = map(int, input().split())
rows = [input().strip() for _ in range(R)]

# 각 칸의 알파벳을 미리 비트로 변환해 둔다. (ord() 비용 제거)
cell = [[1 << (ord(ch) - 65) for ch in row] for row in rows]

DR = (-1, 1, 0, 0)
DC = (0, 0, -1, 1)

answer = 1

# dfs + 비트마스크 (최적화)
def dfs(r: int, c: int, mask: int, depth: int) -> None:
    global answer
    if depth > answer:
        answer = depth
        if answer == 26:
            return
    if answer ==  26:
        return

    # 지역 변수로 바인딩(속도 미세 최적화)
    Rl, Cl = R, C
    DRl, DCl = DR, DC
    celll = cell

    for k in range(4):
        nr = r + DRl[k]
        nc = c + DCl[k]
        if 0 <= nr < Rl  and 0 <= nc < Cl:
            nb = celll[nr][nc]
            if not (mask & nb):
                dfs(nr, nc, mask | nb, depth + 1)

start_mask = cell[0][0]
dfs(0, 0, start_mask, 1)
print(answer)