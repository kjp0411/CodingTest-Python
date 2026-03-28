# https://www.acmicpc.net/problem/12891
S, P = map(int, input().split())
DNA = list(input())
checkList = list(map(int, input().split()))
count = 0

def get_idx(c):
    if c == 'A':
        return 0
    elif c == 'C':
        return 1
    elif c == 'G':
        return 2
    elif c == 'T':
        return 3
    else:
        return

def check():
    for i in range(4):
        if current[i] < checkList[i]:
            return False
    return True


current = [0, 0, 0, 0]

# 초기 윈도우 생성
for i in range(P):
    current[get_idx(DNA[i])] += 1

# 검사
if check():
    count += 1

for i in range(P, S):
    # 추가
    current[get_idx(DNA[i])] += 1

    # 제거
    current[get_idx(DNA[i-P])] -= 1

    # 검사
    if check():
        count += 1

print(count)