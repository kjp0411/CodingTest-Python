# https://www.acmicpc.net/problem/14891
gears = [list(input().strip()) for _ in range(4)]

def rotate(g, dir):
    if dir == 1:    # 시계 방향
        return [g[-1]] + g[:-1]
    else:           # 반시계 방향
        return g[1:] + [g[0]]

K = int(input())

for _ in range(K):
    num, dir = map(int, input().split())
    num -= 1

    dirs = [0] * 4
    dirs[num] = dir

    # 왼쪽 전파
    tmp = dir
    for i in range(num-1, -1, -1):
        if gears[i][2] != gears[i+1][6]:
            tmp = -tmp
            dirs[i] = tmp
        else:
            break

    # 오른쪽 전파
    tmp = dir
    for i in range(num+1, 4):
        if gears[i-1][2] != gears[i][6]:
            tmp = -tmp
            dirs[i] = tmp
        else:
            break

    # 실제 회전 실행
    for i in range(4):
        if dirs[i] != 0:
            gears[i] = rotate(gears[i], dirs[i])

# 점수 계산
score = 0
if gears[0][0] == '1': score += 1
if gears[1][0] == '1': score += 2
if gears[2][0] == '1': score += 4
if gears[3][0] == '1': score += 8

print(score)