# https://www.acmicpc.net/problem/1744
from queue import PriorityQueue
N = int(input())
plusPq = PriorityQueue()
minusPq = PriorityQueue()
one = 0
zero = 0

for i in range(N):              # 4가지로 데이터 분리 저장
    data = int(input())
    if data > 1:
        plusPq.put(data * -1)   # 양수 내림차순 정렬을 위해 -1 곱하여 저장
    elif data == 1:
        one += 1
    elif data == 0:
        zero += 1
    else:
        minusPq.put(data)

sum_value = 0

while plusPq.qsize() > 1:       # 양수 처리
    first = plusPq.get() * -1   # 가장 작은 항목(최우선순위)을 꺼내 반환
    second = plusPq.get() * -1
    sum_value += first * second

if plusPq.qsize() > 0:
    sum_value += plusPq.get() * -1

while minusPq.qsize() > 1:      # 음수 처리
    first = minusPq.get()       # 가장 작은 항목(최우선순위)을 꺼내 반환
    second = minusPq.get()
    sum_value += first * second

if minusPq.qsize() > 0:
    if zero == 0:
        sum_value += minusPq.get()

sum_value += one
print(sum_value)