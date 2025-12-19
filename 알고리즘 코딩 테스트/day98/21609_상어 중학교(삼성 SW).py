# https://www.acmicpc.net/problem/21609
# 블록의 종류: 검정(-1), 무지개(0), 일반(1~M), 빈칸(-2)
from collections import deque

# N: 격자 크기, M: 색상 개수
N, M = map(int, input().split())
graph = []

# 상하좌우 이동
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(N):
    graph.append(list(map(int, input().split())))


# (a, b)를 시작점으로 하는 블록 그룹 탐색
def find_group(a, b):
    # BFS용 방문 배열 (이 함수 안에서만 사용)
    visited = [[False] * N for _ in range(N)]
    groupQ = []  # 현재 블록 그룹 좌표 저장

    # 검정 블록(-1)이나 빈칸(-2)이면 탐색 불가
    if graph[a][b] == -1 or graph[a][b] == -2:
        return

    # 시작 블록의 색상
    # (문제상 일반 블록에서만 호출되므로 사실상 graph[a][b] > 0)
    if graph[a][b] > 0:
        myColor = graph[a][b]
    else:
        myColor = 0

    cnt = 1  # 그룹에 포함된 블록 개수
    queue = deque()
    queue.append((a, b))
    visited[a][b] = True

    # BFS 시작
    while queue:
        x, y = queue.popleft()
        groupQ.append((x, y))

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 밖이거나 이미 방문한 경우
            if nx < 0 or nx >= N or ny < 0 or ny >= N or visited[nx][ny]:
                continue

            # 검정 블록(-1)이나 빈칸(-2)은 포함 불가
            if graph[nx][ny] == -1 or graph[nx][ny] == -2:
                continue

            # 일반 블록인 경우 색상 체크
            if graph[nx][ny] > 0:
                # 아직 색상이 정해지지 않았다면 설정
                if myColor == 0:
                    myColor = graph[nx][ny]
                # 색상이 다르면 포함 불가
                elif myColor != graph[nx][ny]:
                    continue

            # 무지개 블록 또는 같은 색 일반 블록 포함
            cnt += 1
            queue.append((nx, ny))
            visited[nx][ny] = True

    # 블록 수가 2개 미만이면 그룹 아님
    if cnt < 2:
        return

    global groupCnt, maxQ

    # 현재까지 최대 그룹보다 큰 경우
    if cnt > groupCnt:
        groupCnt = cnt
        maxQ = groupQ

    # 블록 개수가 같은 경우 → 무지개 블록 수 비교
    elif cnt == groupCnt:
        thisZeroCnt, maxZeroCnt = 0, 0

        # 현재 그룹의 무지개 개수
        for i in range(cnt):
            if graph[groupQ[i][0]][groupQ[i][1]] == 0:
                thisZeroCnt += 1

        # 기존 최대 그룹의 무지개 개수
        for i in range(groupCnt):
            if graph[maxQ[i][0]][maxQ[i][1]] == 0:
                maxZeroCnt += 1

        # 무지개 개수까지 같은 경우 → 기준 블록 비교
        if thisZeroCnt == maxZeroCnt:
            # 좌표 정렬 (행 우선, 열 차선)
            groupQ.sort(key=lambda x: x[1])
            groupQ.sort(key=lambda x: x[0])
            maxQ.sort(key=lambda x: x[1])
            maxQ.sort(key=lambda x: x[0])

            gx, gy, mx, my = 0, 0, 0, 0

            # 현재 그룹의 기준 블록 (무지개 제외, 행 가장 큰)
            for i in range(cnt):
                if graph[groupQ[i][0]][groupQ[i][1]] != 0:
                    gx = groupQ[i][0]
                    gy = groupQ[i][1]
                    break

            # 기존 최대 그룹의 기준 블록
            for i in range(groupCnt):
                if graph[maxQ[i][0]][maxQ[i][1]] != 0:
                    mx = maxQ[i][0]
                    my = maxQ[i][1]
                    break

            # 기준 블록 행/열 비교
            if gx > mx:
                maxQ = groupQ
            elif gx == mx:
                if gy > my:
                    maxQ = groupQ

        # 무지개 블록이 더 많은 경우
        elif thisZeroCnt > maxZeroCnt:
            maxQ = groupQ

    return


# 중력 적용 함수
def gravity():
    # 아래에서 위로 검사
    for i in range(N - 2, -1, -1):
        for j in range(N):
            # 검정 블록은 움직이지 않음
            if graph[i][j] != -1:
                tmp = i
                # 아래가 빈칸(-2)이면 계속 떨어뜨림
                while tmp + 1 < N and graph[tmp + 1][j] == -2:
                    graph[tmp + 1][j] = graph[tmp][j]
                    graph[tmp][j] = -2
                    tmp += 1


# 반시계 방향 90도 회전
def rotate():
    newGraph = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            newGraph[N - 1 - j][i] = graph[i][j]
    return newGraph


answer = 0

# 메인 게임 루프
while True:
    groupCnt = 0  # 현재 가장 큰 그룹 크기
    maxQ = []     # 가장 큰 그룹 좌표 목록

    # 모든 칸을 시작점으로 그룹 탐색
    for i in range(N):
        for j in range(N):
            if graph[i][j] > 0:  # 일반 블록만 시작점
                find_group(i, j)

    # 더 이상 제거할 그룹이 없으면 종료
    if not maxQ:
        break

    # 점수 획득
    answer += len(maxQ) ** 2

    # 블록 제거
    for x, y in maxQ:
        graph[x][y] = -2

    # 중력 → 회전 → 중력
    gravity()
    graph = rotate()
    gravity()

print(answer)