# https://www.acmicpc.net/problem/1427
A = list(input())

for i in range(len(A)):
    Max_value = i
    for j in range(i+1, len(A)):
        if A[j] > A[Max_value]:
            Max_value = j
    if A[i] < A[Max_value]:
        temp = A[i]
        A[i] = A[Max_value]
        A[Max_value] = temp

print(''.join(map(str, A)))
