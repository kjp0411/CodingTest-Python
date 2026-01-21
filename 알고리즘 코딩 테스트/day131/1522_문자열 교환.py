# https://www.acmicpc.net/problem/1522
S = input()
A_count = S.count('a')
S = S + S
B_count = S[0:A_count].count('b')
min_B_count = B_count

for l in range(1, len(S)//2):
    r = l + A_count - 1

    if S[l-1] == 'b':
        B_count -= 1

    if S[r] == 'b':
        B_count += 1

    if B_count < min_B_count:
        min_B_count = B_count

print(min_B_count)