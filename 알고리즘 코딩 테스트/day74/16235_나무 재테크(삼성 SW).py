# https://www.acmicpc.net/problem/16235
# Python 3 시간 초과 -> PyPy3 통과
# 나무 재테크

# 봄에는 나무가 자신의 나이만큼 양분을 먹고, 나이 1 증가
# 각각의 나무는 위치한 칸에 있는 양분만 먹을 수 있음
# (하나의 칸에 여러 개의 나무가 있다면, 어린 나무부터 양분을 먹음)
# (땅에 양분이 부족해서 자신의 나이만큼 양분을 먹지 못하면 죽음)

# 여름에는 봄에 죽은 나무가 양분으로 변함
# 각각의 죽은 나무마다 나이를 2로 나눈 값이 나무가 있던 칸에 양분으로 추가
# (소수점 아래는 버림)

# 가을에는 나무가 번식함
# 번식하는 나무는 나이가 5의 배수이어야 하며,
# 인접한 8개의 칸에 나이가 1인 나무가 생김

# 겨울에는 땅을 돌아다니면서 땅에 양분을 추가함

# K년이 지난 후 땅에 살아있는 나무의 개수를 구하시오.
N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
nutrition = [[5] * N for _ in range(N)]     # 초기 양분 5
forest = [[[] for _ in range(N)] for _ in range(N)]

for _ in range(M):
    x, y, z = map(int, input().split())
    forest[x-1][y-1].append(z)

def spring():
    global forest, nutrition
    dead = []   # 여름에서 사용될 죽은 나무 목록 (x, y, age)

    for i in range(N):
        for j in range(N):
            if forest[i][j]:
                forest[i][j].sort() # 어린 나무부터 먹을 수 있게 정렬

                alive = []
                for age in forest[i][j]:
                    if nutrition[i][j] >= age:
                        nutrition[i][j] -= age
                        alive.append(age + 1)
                    else:
                        dead.append((i, j, age))

                forest[i][j] = alive
    return dead

def summer(dead):
    global nutrition
    for x, y, age in dead:
        nutrition[x][y] += age // 2

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]
def fall():
    global forest
    for i in range(N):
        for j in range(N):
            for age in forest[i][j]:
                if age % 5 == 0:
                    for k in range(8):
                        nx = i + dx[k]
                        ny = j + dy[k]
                        if 0 <= nx < N and 0 <= ny < N:
                            forest[nx][ny].append(1)
def winter():
    global nutrition
    for i in range(N):
        for j in range(N):
            nutrition[i][j] += A[i][j]

for _ in range(K):
    dead = spring()
    summer(dead)
    fall()
    winter()

answer = 0
for i in range(N):
    for j in range(N):
        answer += len(forest[i][j])

print(answer)