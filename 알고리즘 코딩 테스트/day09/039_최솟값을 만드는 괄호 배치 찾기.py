# https://www.acmicpc.net/problem/1541
answer = 0
A = list(map(str, input().split("-")))

def mySum(i):
    sum_value = 0
    temp = str(i).split("+")
    for i in temp:
        sum_value += int(i)
    return sum_value

for i in range(len(A)):
    temp = mySum(A[i])
    if i == 0:
        answer += temp  # 가장 앞에 있는 값만 더하기
    else:
        answer -= temp  # 뒷부분의 값은 합쳐서 빼기

print(answer)