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
        answer += temp
    else:
        answer -= temp

print(answer)