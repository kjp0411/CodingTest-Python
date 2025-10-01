# https://www.acmicpc.net/problem/10868
import sys
input = sys.stdin.readline
# 수의 개수, 최솟값을 구하는 횟수
N, M = map(int, input().split())
treeHeight = 0
length = N

while length != 0:
    length //= 2
    treeHeight += 1

treeSize = pow(2, treeHeight + 1)
leftNodeStartIndex = treeSize // 2 - 1
tree = [sys.maxsize] * treeSize

# 데이터를 리프 노드에 저장
for i in range(leftNodeStartIndex + 1, leftNodeStartIndex + N + 1):
    tree[i] = int(input())

# 인덱스 트리 생성 함수
def setTree(i):
    while i != 1:
        if tree[i // 2]> tree[i]:
            tree[i // 2] = tree[i]
        i -= 1

setTree(treeSize - 1)

# 최솟값 계산 함수
def getMin(s, e):
    min_value = sys.maxsize
    while s <= e:
        if s % 2 == 1:
            min_value = min(min_value, tree[s])
            s += 1
        if e % 2 == 0:
            min_value = min(min_value, tree[e])
            e -= 1
        s = s // 2
        e = e // 2
    return min_value

for _ in range(M):
    s, e = map(int, input().split())
    s = s + leftNodeStartIndex
    e = e + leftNodeStartIndex
    print(getMin(s, e))