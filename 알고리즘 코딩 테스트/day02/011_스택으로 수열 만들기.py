# https://www.acmicpc.net/problem/1874
n = int(input())
A = [0] * n

for i in range(n):
    A[i] = int(input())

stack = []
num = 1
answer = []
result = True

for i in range(n):
    su = A[i]
    if su >= num:   # 현재 수열값 >= 오름차순 자연수: 값이 같아질 때까지 append() 수행
        while su >= num:
            stack.append(num)
            num += 1
            answer.append('+')
        stack.pop()
        answer.append('-')
    else:           # 현재 수열값 < 오름차순 자연수: pop()을 수행해 수열 원소를 꺼냄
        n = stack.pop()
        # 스택의 가장 위의 수가 만들어야 하는 수열의 수보다 크면 수열을 출력할 수 없음
        if n > su:
            print("NO")
            result = False
            break
        else:
            answer.append('-')

if result:
    for i in answer:
        print(i)