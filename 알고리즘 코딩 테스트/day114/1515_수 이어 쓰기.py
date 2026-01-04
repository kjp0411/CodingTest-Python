# https://www.acmicpc.net/problem/1515
s = input()
idx = 0
num = 1

while idx < len(s):
    for ch in str(num):
        if idx < len(s) and ch == s[idx]:
            idx += 1
    num += 1

print(num - 1)