# https://www.acmicpc.net/problem/21921
import sys
input = sys.stdin.readline

N, X = map(int, input().split())
visitors = list(map(int, input().split()))

# 1. 초기 X일 방문자 수
current_sum = sum(visitors[:X])
max_sum = current_sum
count = 1

# 2. 슬라이딩 윈도우
for i in range(X, N):
    current_sum += visitors[i]
    current_sum -= visitors[i - X]

    if current_sum > max_sum:
        max_sum = current_sum
        count = 1
    elif current_sum == max_sum:
        count += 1

# 3. 출력
if max_sum == 0:
    print("SAD")
else:
    print(max_sum)
    print(count)