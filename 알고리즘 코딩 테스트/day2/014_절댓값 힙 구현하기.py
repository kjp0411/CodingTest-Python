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
            temp = myQueue.get()
            print(str(temp[1]) + '\n')
    else:
        # 절댓값을 기준으로 정렬하고 같으면 음수 우선 정렬하도록 구성
        myQueue.put((abs(request), request))