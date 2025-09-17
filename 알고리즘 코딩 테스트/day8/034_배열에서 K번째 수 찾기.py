# https://www.acmicpc.net/problem/1300
N = int(input())
K = int(input())
start = 1
end = K
ans = 0

# 이진 탐색 수행
while start <= end:
    middle = int((start + end) / 2)
    cnt = 0
    # 중앙값보다 작은 수 계산
    for i in range(1, N + 1):
        cnt += min(int(middle/ i), N)
    if cnt < K:
        start = middle + 1
    else:
        ans = middle
        end = middle - 1

print(ans)