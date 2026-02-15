# https://www.acmicpc.net/problem/20437
import sys
input = sys.stdin.readline

T = int(input().strip())

for _ in range(T):
    positions = {}
    max_length = -1
    min_length = 10**9
    w = list(input().strip())
    k = int(input().strip())

    for idx, ch in enumerate(w):
        if ch not in positions:
            positions[ch] = []
        positions[ch].append(idx)

        if len(positions[ch]) >= k:
            m = len(positions[ch])
            length = positions[ch][m-1] - positions[ch][m-k] + 1

            if length > max_length:
                max_length = length

            if length < min_length:
                min_length = length

    if max_length == -1:
        print(-1)
    else:
        print(min_length, max_length)
