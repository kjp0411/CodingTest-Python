# https://www.acmicpc.net/problem/2110
N, C = map(int, input().split())
houses = []
for _ in range(N):
    houses.append(int(input()))
houses = sorted(houses)

start = 1
end = houses[-1] - houses[0]
answer = 0

while start <= end:
    mid = (start + end) // 2
    count = 1   # 1번째 집에 무조건 설치
    last = houses[0]

    for i in range(1, N):
        if houses[i] - last >= mid:
            count += 1
            last = houses[i]

    if count >= C:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)