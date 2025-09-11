# https://www.acmicpc.net/problem/2164
from collections import deque
N = int(input())
myDeque = deque()

for i in range(1, N+1):
    myDeque.append(i)

while len(myDeque) > 1:
    myDeque.popleft()
    myDeque.append(myDeque.popleft())

print(myDeque[0])