# https://www.acmicpc.net/problem/19237
N,M,K=map(int,input().split())

dx=[0,-1,1,0,0]
dy=[0,0,0,-1,1]

smellBoard=[[[0]*2 for _ in range(N)] for _ in range(N)]
board=[]
sharkInfo=dict()
for i in range(N):
    arr=list(map(int,input().split()))
    for j in range(N):
        if arr[j]>0:
            sharkInfo[arr[j]]=dict()
            sharkInfo[arr[j]]["pos"]=[i,j]
    board.append(arr)

nowDir=list(map(int,input().split()))
for i in range(1,M+1):
    sharkInfo[i]["dir"]=nowDir[i-1]

for i in range(1,M+1):
    sharkInfo[i]["dirPrior"]=dict()
    for j in range(1,5):
        sharkInfo[i]["dirPrior"][j]=list(map(int,input().split()))

def spreadSmell(smellBoard,sharkInfo):
    for key in sharkInfo.keys():
        x,y=sharkInfo[key]["pos"]
        smellBoard[x][y][0]=key
        smellBoard[x][y][1]=K

def moveShark(smellBoard,sharkInfo,board):
    newBoard=[[0]*N for _ in range(N)]
    deleteList=[]
    for key in sharkInfo.keys():
        x,y=sharkInfo[key]["pos"]
        dir=sharkInfo[key]["dir"]
        dirPrior=sharkInfo[key]["dirPrior"]
        possibleBlock=[]
        for i in range(4):
            nx=x+dx[dirPrior[dir][i]]
            ny=y+dy[dirPrior[dir][i]]
            if nx<0 or ny<0 or nx>=N or ny>=N:
                continue
            if smellBoard[nx][ny][0]==0:
                possibleBlock.append((0,i,dirPrior[dir][i],[nx,ny]))
            elif smellBoard[nx][ny][0]==key:
                possibleBlock.append((1,i,dirPrior[dir][i],[nx,ny]))
        next=sorted(possibleBlock)[0]
        sharkInfo[key]["pos"]=next[3]
        sharkInfo[key]["dir"]=next[2]
        nx,ny=next[3]
        if newBoard[nx][ny]==0:
            newBoard[nx][ny]=key
        elif newBoard[nx][ny]>key:
            deleteList.append(newBoard[nx][ny])
            newBoard[nx][ny]=key
        elif newBoard[nx][ny]<key:
            deleteList.append(key)
    for key in deleteList:
        del sharkInfo[key]
    return newBoard

def minusSmell(smellBoard):
    for i in range(N):
        for j in range(N):
            if smellBoard[i][j][0]!=0:
                if smellBoard[i][j][1]>1:
                    smellBoard[i][j][1]-=1
                elif smellBoard[i][j][1]==1:
                    smellBoard[i][j]=[0,0]
t=0
while t<=1000:
    spreadSmell(smellBoard,sharkInfo)
    board=moveShark(smellBoard,sharkInfo,board)
    minusSmell(smellBoard)
    t+=1
    if len(sharkInfo)==1:
        break

if t==1001:
    print(-1)
else:
    print(t)