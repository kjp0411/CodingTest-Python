# https://www.acmicpc.net/problem/11286
from queue import PriorityQueue
import sys

input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
myQueue = PriorityQueue()

for i in range(N):
    request = int(input())
    if request == 0:
        if myQueue.empty():
            print('0\n')
        else:
            print(str(myQueue.get()[1]) + '\n')
    else:
        myQueue.put((abs(request), request))