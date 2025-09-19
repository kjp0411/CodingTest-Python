# https://www.acmicpc.net/problem/2018
N = int(input())
count, start_idx, end_idx, sum_value = 1, 1, 1, 1

while end_idx != N:
    if sum_value == N:
        count += 1
        end_idx += 1
        sum_value += end_idx
    elif sum_value > N:
        sum_value -= start_idx
        start_idx += 1
    else:
        end_idx += 1
        sum_value += end_idx
print(count)