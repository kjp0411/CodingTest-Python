# https://www.acmicpc.net/problem/1546
N = int(input())
grades = list(map(int, input().split()))
max_grade = max(grades)

average = sum(grades) * 100 / max_grade / N
print(average)
