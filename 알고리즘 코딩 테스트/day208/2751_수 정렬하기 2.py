# https://www.acmicpc.net/problem/2751
import sys
input = sys.stdin.readline

N = int(input())
A = [0] * N

for i in range(N):
    A[i] = int(input())

def merge_sort(arr):
    if len(arr) == 1:
        return arr
    else:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        left = merge_sort(left)
        right = merge_sort(right)
        result = []
        i = 0
        j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result += left[i:]
        result += right[j:]
    return result

print('\n'.join(map(str, merge_sort(A))))