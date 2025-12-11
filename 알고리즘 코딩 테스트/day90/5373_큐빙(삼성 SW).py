# https://www.acmicpc.net/problem/5373
import sys


def turn_itselt(i):
    global cube
    temp = cube[i][0][0]
    cube[i][0][0] = cube[i][2][0]
    cube[i][2][0] = cube[i][2][2]
    cube[i][2][2] = cube[i][0][2]
    cube[i][0][2] = temp
    temp = cube[i][0][1]
    cube[i][0][1] = cube[i][1][0]
    cube[i][1][0] = cube[i][2][1]
    cube[i][2][1] = cube[i][1][2]
    cube[i][1][2] = temp


def turn(side, direction):
    if direction == '+':
        if side == 'U':
            turn_itselt(0)  # 위
            temp = cube[2][0]
            cube[2][0] = cube[5][0]
            cube[5][0] = cube[3][0]
            cube[3][0] = cube[4][0]
            cube[4][0] = temp

        if side == 'F':
            turn_itselt(2)  # 앞
            temp = cube[0][2]
            cube[0][2] = [cube[4][2][2], cube[4][1][2], cube[4][0][2]]
            cube[4][0][2], cube[4][1][2], cube[4][2][2] = [cube[1][0][0], cube[1][0][1], cube[1][0][2]]
            cube[1][0][0], cube[1][0][1], cube[1][0][2] = [cube[5][2][0], cube[5][1][0], cube[5][0][0]]
            cube[5][0][0], cube[5][1][0], cube[5][2][0] = [temp[0], temp[1], temp[2]]
        if side == 'R':
            turn_itselt(5)  # 오른쪽
            temp = [cube[0][0][2], cube[0][1][2], cube[0][2][2]]
            cube[0][0][2], cube[0][1][2], cube[0][2][2] = [cube[2][0][2], cube[2][1][2], cube[2][2][2]]
            cube[2][0][2], cube[2][1][2], cube[2][2][2] = [cube[1][0][2], cube[1][1][2], cube[1][2][2]]
            cube[1][0][2], cube[1][1][2], cube[1][2][2] = [cube[3][2][0], cube[3][1][0], cube[3][0][0]]
            cube[3][2][0], cube[3][1][0], cube[3][0][0] = [temp[0], temp[1], temp[2]]
        if side == 'B':
            turn_itselt(3)  # 뒤
            temp = cube[0][0]
            cube[0][0] = [cube[5][0][2], cube[5][1][2], cube[5][2][2]]
            cube[5][0][2], cube[5][1][2], cube[5][2][2] = [cube[1][2][2], cube[1][2][1], cube[1][2][0]]
            cube[1][2][2], cube[1][2][1], cube[1][2][0] = [cube[4][2][0], cube[4][1][0], cube[4][0][0]]
            cube[4][2][0], cube[4][1][0], cube[4][0][0] = [temp[0], temp[1], temp[2]]
        if side == 'L':
            turn_itselt(4)  # 왼쪽
            temp = [cube[0][0][0], cube[0][1][0], cube[0][2][0]]
            cube[0][2][0], cube[0][1][0], cube[0][0][0] = [cube[3][0][2], cube[3][1][2], cube[3][2][2]]  # 반전
            cube[3][0][2], cube[3][1][2], cube[3][2][2] = [cube[1][2][0], cube[1][1][0], cube[1][0][0]]  # 반전
            cube[1][0][0], cube[1][1][0], cube[1][2][0] = [cube[2][0][0], cube[2][1][0], cube[2][2][0]]
            cube[2][0][0], cube[2][1][0], cube[2][2][0] = [temp[0], temp[1], temp[2]]  # 반전
        if side == 'D':
            turn_itselt(1)
            temp = cube[2][2]
            cube[2][2] = cube[4][2]
            cube[4][2] = cube[3][2]
            cube[3][2] = cube[5][2]
            cube[5][2] = temp
    elif direction == '-':
        turn(side, '+')
        turn(side, '+')
        turn(side, '+')


N = int(sys.stdin.readline())
for _ in range(N):
    Tastcase_N = int(sys.stdin.readline())
    cube = [[] for t in range(6)]
    for t in range(3):
        cube[0].append(['w', 'w', 'w'])
        cube[1].append(['y', 'y', 'y'])
        cube[2].append(['r', 'r', 'r'])
        cube[3].append(['o', 'o', 'o'])
        cube[4].append(['g', 'g', 'g'])
        cube[5].append(['b', 'b', 'b'])
    testcase = list(map(str, sys.stdin.readline().rstrip().split()))  # testcase 저장
    for test in testcase:
        turn(test[0], test[1])
    for i in range(3):
        for j in range(3):
            print(cube[0][i][j], end="")
        print()