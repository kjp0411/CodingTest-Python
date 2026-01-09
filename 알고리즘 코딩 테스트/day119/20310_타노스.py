# https://www.acmicpc.net/problem/20310
S = list(input())

remove_one = S.count('1') // 2
remove_zero = S.count('0') // 2

# 앞에서 1 제거
i = 0
while remove_one:
    if S[i] == '1':
        S[i] = ''
        remove_one -= 1
    i += 1

# 뒤에서 0 제거
i = len(S) - 1
while remove_zero:
    if S[i] == '0':
        S[i] = ''
        remove_zero -= 1
    i -= 1

print(''.join(S))