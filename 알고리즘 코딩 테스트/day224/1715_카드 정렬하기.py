# https://www.acmicpc.net/problem/1715
from queue import PriorityQueue
N = int(input())
pq = PriorityQueue()

for _ in range(N):
    date = int(input())
    pq.put(date)

data1 = 0
data2 = 0
sum_value = 0

while pq.qsize() > 1:
    data1 = pq.get()
    data2 = pq.get()
    temp = data1 + data2
    sum_value += temp
    pq.put(temp)

print(sum_value)