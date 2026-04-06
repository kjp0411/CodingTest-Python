# https://www.acmicpc.net/problem/11399
N = int(input())
A = list(map(int, input().split()))

for i in range(N):
    insert_point = i
    insert_value = A[i]
    for j in range(i-1, -1, -1):
        if A[j] > insert_value:
            A[j+1] = A[j]
            insert_point = j
    A[insert_point] = insert_value

temp = 0
time = 0
for i in range(N):
    temp += A[i]
    time += temp
print(time)