# https://www.acmicpc.net/problem/2751
# # 코드1 (시간 초과)
# N = int(input())
# A = [0] * N
# for i in range(N):
#     A[i] = int(input())
#
# A = sorted(A, reverse=False)
#
# for i in range(N):
#     print(A[i])

# 코드2(병합 정렬) 메모리: 79784KB 시간: 5424ms
import sys
input = sys.stdin.readline
print = sys.stdout.write

def merge_sort(s, e):   # 병합 정렬 수행
    if e - s < 1:
        return
    m = int(s + (e - s) / 2)
    merge_sort(s, m)
    merge_sort(m + 1, e)
    for i in range(s, e + 1):
        tmp[i] = A[i]
    k = s
    index1 = s
    index2 = m+1
    while index1 <= m and index2 <= e:  # 두 그룹을 병합하는 로직
        if tmp[index1] > tmp[index2]:
            A[k] = tmp[index2]
            k += 1
            index2 += 1
        else:
            A[k] = tmp[index1]
            k += 1
            index1 += 1

    while index1 <= m:
        A[k] = tmp[index1]
        k += 1
        index1 += 1

    while index2 <= e:
        A[k] = tmp[index2]
        k += 1
        index2 += 1

N = int(input())
A = [0] * int(N + 1)
tmp = [0] * int(N + 1)

for i in range(1, N + 1):
    A[i] = int(input())

merge_sort(1, N)

for i in range(1, N + 1):
    print(str(A[i]) + '\n')