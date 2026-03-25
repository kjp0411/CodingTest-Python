# https://www.acmicpc.net/problem/2018
N = int(input())

count = 0
l = 1       # 자연수는 1부터 시작
r = 1       # 자연수는 1부터 시작

sum_value = 1   # r의 1은 더하고 시작

while r <= N:
    if sum_value == N:
        count += 1
        r += 1
        sum_value += r
    elif sum_value > N:
        sum_value -= l
        l += 1
    else:
        r += 1
        sum_value += r
print(count)