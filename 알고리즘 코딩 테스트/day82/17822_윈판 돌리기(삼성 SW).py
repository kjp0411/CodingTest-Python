# https://www.acmicpc.net/problem/17822
import sys
input = sys.stdin.readline

N, M, T = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
ops = [list(map(int, input().split())) for _ in range(T)]

# 회전 함수
def rotate(A, x, d, k):
    for i in range(x-1, N, x):      # x의 배수인 원판만 회전
        k_mod = k % M               # M보다 큰 k 대비
        if d == 0:  # 시계 방향
            A[i] = A[i][-k_mod:] + A[i][:-k_mod]
        else:       # 반시계 방향
            A[i] = A[i][k_mod:] + A[i][:k_mod]

# 인접 동일 숫자 제거 함수
def remove_adjacent(A):
    remove_set = set()
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for i in range(N):
        for j in range(M):
            if A[i][j] == 0:
                continue

            for dx, dy in directions:
                ni = i + dx
                nj = (j + dy) % M   # 원형이므로 % M 적용

                if 0 <= ni < N and A[ni][nj] == A[i][j]:
                    remove_set.add((i, j))
                    remove_set.add((ni, nj))

    # 지울 것이 있으면 모두 0으로 만듦
    for i, j in remove_set:
        A[i][j] = 0

    return len(remove_set) > 0  # 제거 여부 반환

# 제거 없으면 평균으로 조정하는 함수
def adjust_by_average(A):
    total = 0
    cnt = 0

    for i in range(N):
        for j in range(M):
            if A[i][j] != 0:
                total += A[i][j]
                cnt += 1

    if cnt == 0:
        return

    avg = total / cnt

    for i in range(N):
        for j in range(M):
            if A[i][j] == 0:
                continue
            if A[i][j] > avg:
                A[i][j] -= 1
            elif A[i][j] < avg:
                A[i][j] += 1

for x, d, k in ops:
    rotate(A, x, d, k)

    removed = remove_adjacent(A)

    if not removed:
        adjust_by_average(A)

answer = sum(sum(row) for row in A)
print(answer)