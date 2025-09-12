# https://www.acmicpc.net/problem/1427
import sys
print = sys.stdout.write
A = list(input())

for i in range(len(A)):
    Max = i
    for j in range(i+1, len(A)):
        if A[j] > A[Max]:
            Max = j
    if A[i] < A[Max]:
        temp = A[i]
        A[i] = A[Max]
        A[Max] = temp

for i in range(len(A)):
    print(A[i])