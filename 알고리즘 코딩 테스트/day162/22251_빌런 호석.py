# https://www.acmicpc.net/problem/22251
# N: 최대 층, K: 자릿 수, P: 최대 반전 수, X: 현재 층
N, K, P, X = map(int, input().split())

# 표준 7세그먼트
nums = [
    0b1111110,  # 0
    0b0110000,  # 1
    0b1101101,  # 2
    0b1111001,  # 3
    0b0110011,  # 4
    0b1011011,  # 5
    0b1011111,  # 6
    0b1110000,  # 7
    0b1111111,  # 8
    0b1111011,  # 9
]

cost = [[0] * 10 for _ in range(10)]

for a in range(10):
    for b in range(10):
        cost[a][b] = bin(nums[a] ^ nums[b]).count('1')

count = 0

x_str = str(X).zfill(K)         # X를 K자리 고정

for f in range(1, N+1):
    if f == X:
        continue

    f_str = str(f).zfill(K)     # F를 K자리 고정
    flips = 0

    for i in range(K):
        xd = int(x_str[i])      # X의 i번째 자리 숫자
        fd = int(f_str[i])      # F의 i번째 자리 숫자

        flips += cost[xd][fd]

        if flips > P:
            break

    if 1 <= flips <= P:
        count += 1

print(count)