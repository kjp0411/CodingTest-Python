# https://www.acmicpc.net/problem/20061
import sys
import copy

input=sys.stdin.readline

def setXYBlock(t,x,y):
    if t==1:
        return [[x,y]]

    elif t==2:
        return [[x,y],[x,y+1]]

    elif t==3:
        return [[x,y],[x+1,y]]

def setBlock(posBlock):
    posBlock2=[]

    for x,y in posBlock:
        posBlock2.append([y,3-x])

    minB1,minB2=4,4
    for x,y in posBlock:
        minB1=min(minB1,x)

    for x,y in posBlock2:
        minB2=min(minB2,x)

    for i in range(len(posBlock)):
        posBlock[i][0]-=minB1
        posBlock2[i][0]-=minB2

    return [posBlock,posBlock2]

def goBlock(board,block):
    prev=copy.deepcopy(block)

    while True:
        for i in range(len(block)):
            block[i][0]+=1
        canPut=True

        for i in range(len(block)):
            if block[i][0]>=6 or board[block[i][0]][block[i][1]]==1:
                canPut=False
                break

        if canPut:
            prev=copy.deepcopy(block)

        else:
            break

    for i in range(len(prev)):
        board[prev[i][0]][prev[i][1]]=1

n=int(input())
board=[[[0]*4 for _ in range(6)] for _ in range(2)]

def getScore(board):
    global score
    new_board=[[0]*4 for _ in range(6)]
    fillIndex=5

    for i in range(5,-1,-1):
        full=True
        for j in range(4):
            if board[i][j]!=1:
                full=False
                break

        if full:
            score+=1
            continue

        for j in range(4):
            new_board[fillIndex][j]=board[i][j]

        fillIndex-=1

    return new_board

def deleteBlock(board):
    new_board=[[0]*4 for _ in range(6)]
    check=0

    for i in range(2):
        for j in range(4):
            if board[i][j]==1:
                check+=1
                break

    if check==0:
        return board

    for i in range(5-check,-1,-1):
        for j in range(4):
            new_board[i+check][j]=board[i][j]

    return new_board

score=0

for _ in range(n):
    t,x,y=map(int,input().split())
    posBlock=setXYBlock(t,x,y)
    downBlocks=setBlock(posBlock)

    for i in range(2):
        goBlock(board[i],downBlocks[i])
        board[i]=getScore(board[i])
        board[i]=deleteBlock(board[i])

cnt=0
for i in range(2):
    for a in range(2,6):
        for b in range(4):
            if board[i][a][b]==1:
                cnt+=1

print(score)
print(cnt)