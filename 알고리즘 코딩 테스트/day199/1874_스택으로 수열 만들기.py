# https://www.acmicpc.net/problem/1874
N = int(input())
stack = []
nums = []
answer = []
for _ in range(N):
    nums.append(int(input().strip()))

num = 1

for target in nums:
    while num <= target:
        stack.append(num)
        answer.append('+')
        num += 1
    if stack[-1] == target:
        stack.pop()
        answer.append('-')
    else:
        print("NO")
        exit()

for a in answer:
    print(a)