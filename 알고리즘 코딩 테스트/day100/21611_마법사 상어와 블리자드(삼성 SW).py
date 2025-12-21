# https://www.acmicpc.net/problem/21611
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
magics = [tuple(map(int, input().split())) for _ in range(M)]

# dr(세로), dc(가로)
dr = [0, -1, 1, 0, 0]
dc = [0, 0, 0, -1, 1]

def get_spiral_order():
    # 나선형 이동 방향: 좌, 하, 우, 상
    sdr = [0, 1, 0, -1]
    sdc = [-1, 0, 1, 0]

    r, c = N // 2, N // 2
    order = []
    dist = 1
    d = 0

    while True:
        for _ in range(2):  # 한 거리당 두 번씩 방향 전환
            for _ in range(dist):
                r += sdr[d]
                c += sdc[d]
                if 0 <= r < N and 0 <= c < N:
                    order.append((r, c))
                else:
                    return order
            d = (d + 1) % 4
        dist += 1

order = get_spiral_order()

def get_beads():
    beads = []
    for r, c in order:
        if board[r][c] == 0: break  # 구슬이 없는 경우
        beads.append(board[r][c])
    return beads

# 블리자드 마법(구슬 파괴)
def blizzard(d, s):
    r, c = N // 2, N // 2
    for i in range(1, s + 1):
        nr, nc = r + dr[d] * i, c + dc[d] * i
        if 0 <= nr < N and 0 <= nc < N:
            board[nr][nc] = 0

# 구슬의 이동 및 폭발
def solve_beads(beads):
    global answer
    while True:
        # 1. 빈칸 채우기
        beads = [b for b in beads if b != 0]

        # 2. 4개 이상 연속된 구술 찾아서 폭발
        if not beads: break

        exploded = False
        new_beads = []
        i = 0
        while i < len(beads):
            target = beads[i]
            count = 1
            j = i + 1
            while j < len(beads) and beads[j] == target:
                count += 1
                j += 1

            if count >= 4:
                answer += target * count    # 점수 계산
                exploded = True
            else:
                for _ in range(count):
                    new_beads.append(target)
            i = j

        beads = new_beads
        if not exploded: break
    return beads

# 구슬의 변화
def transform_beads(beads):
    new_beads = []
    i = 0
    while i < len(beads):
        target = beads[i]
        count = 1
        j = i + 1
        while j < len(beads) and beads[j] == target:
            count += 1
            j += 1
        new_beads.append(count)
        new_beads.append(target)
        if len(new_beads) >= N*N - 1: break
        i = j

    return new_beads[:N*N - 1]

answer = 0
for d, s in magics:
    # 1. 블리자드 마법으로 구슬 파괴
    blizzard(d, s)

    # 2. 파괴된 후 남은 구슬들을 1차원 리스트로 추출
    beads = []
    for r, c in order:
        if board[r][c] != 0:
            beads.append((board[r][c]))

    # 3. 구슬 폭발 및 이동 처리
    beads = solve_beads(beads)

    # 4. 구슬 변화
    beads = transform_beads(beads)

    # 5. 변화된 beads를 다시 2차원 board에 입히기
    board = [[0] * N for _ in range(N)]
    for i in range(len(beads)):
        r, c = order[i]
        board[r][c] = beads[i]

print(answer)