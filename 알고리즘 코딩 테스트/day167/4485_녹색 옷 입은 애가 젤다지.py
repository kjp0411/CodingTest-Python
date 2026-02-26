# https://www.acmicpc.net/problem/4485
import sys
import heapq
input = sys.stdin.readline
INF = 10**15

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

case = 1

while True:
    N = int(input())

    # 종료 조건 N: 0
    if N == 0:
        break
    dist = [[INF] * N for _ in range(N)]
    board = [list(map(int, input().split())) for _ in range(N)]

    dist[0][0] = board[0][0]    # 시작하자마자 비용 추가

    pq = []
    heapq.heappush(pq, (board[0][0], 0, 0))
    while pq:
        cost, r, c = heapq.heappop(pq)

        if cost > dist[r][c]:
            continue

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                new_cost = cost + board[nr][nc]
                if new_cost < dist[nr][nc]:
                    dist[nr][nc] = new_cost
                    heapq.heappush(pq, (new_cost, nr, nc))

    print("Problem " + str(case) + ": " + str(dist[N-1][N-1]))
    case += 1