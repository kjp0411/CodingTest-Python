# https://www.acmicpc.net/problem/17825
graph = [[] for _ in range(33)]

for i in range(20):
    graph[i].append((i + 1, 2 * (i + 1)))

graph[20].append((21, 0))
graph[5].append((22, 13))
graph[22].append((23, 16))
graph[23].append((24, 19))
graph[24].append((30, 25))

graph[10].append((25, 22))
graph[25].append((26, 24))
graph[26].append((30, 25))

graph[15].append((27, 28))
graph[27].append((28, 27))
graph[28].append((29, 26))
graph[29].append((30, 25))
graph[30].append((31, 30))
graph[31].append((32, 35))
graph[32].append((20, 40))

pos = [0, 0, 0, 0]
arr = list(map(int, input().split()))
answer = 0

def nextGo(nowPos, diceNum):
    s = 0
    if nowPos == 21:
        return 21, 0
    for i in range(diceNum):
        if i == 0 and len(graph[nowPos]) > 1:
            s = graph[nowPos][1][1]
            nowPos = graph[nowPos][1][0]
        else:
            s = graph[nowPos][0][1]
            nowPos = graph[nowPos][0][0]
        if nowPos == 21:
            return 21, 0

    return nowPos, s

def dfs(score, deep):
    global answer
    if deep == len(arr):
        answer = max(answer, score)
        return
    for i in range(4):
        k, s = nextGo(pos[i], arr[deep])
        if k == 21 or k not in pos:
            prev = pos[i]
            pos[i] = k
            dfs(score + s, deep + 1)
            pos[i] = prev
        else:
            continue

dfs(0, 0)
print(answer)