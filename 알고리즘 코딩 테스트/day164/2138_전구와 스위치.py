# https://www.acmicpc.net/problem/2138
N = int(input())
start = list(input().strip())
end = list(input().strip())

# 왼쪽에서 오른쪽으로 2번 진행(동작 1: O, 동작 1: X)
def simulate(case):
    # 0-index 기준
    # 동작 1: 1번 스위치 누르면 0, 1번 전구 상태 바뀜
    # 동작 2: i번 스위치 누르면 i-1, i, i+1 전구 상태 바뀜
    # 동작 3: N번 스위치 누르면 N-2, N-1번 전구 상태 바뀜

    bulbs = start[:]  # 복사
    count = 0

    def toggle(i):
        for j in (i-1, i, i+1):
            if 0 <= j < N:
                bulbs[j] = '1' if bulbs[j] == '0' else '0'

    if case == 1:
        toggle(0)
        count += 1

    for i in range(1, N):
        if bulbs[i-1] != end[i-1]:
            toggle(i)
            count += 1

    if bulbs == end:
        return count
    else:
        return float('inf')

res1 = simulate(0)
res2 = simulate(1)

ans = min(res1, res2)
print(ans if ans != float('inf') else -1)