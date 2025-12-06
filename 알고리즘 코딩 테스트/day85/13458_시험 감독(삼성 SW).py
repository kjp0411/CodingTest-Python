# https://www.acmicpc.net/problem/13458
import math

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

count = 0
for students in A:
    count += 1
    students -= B

    if students > 0:
        count += math.ceil(students / C)
print(count)