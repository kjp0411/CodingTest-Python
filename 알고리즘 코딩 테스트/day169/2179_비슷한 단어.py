# https://www.acmicpc.net/problem/2179
import sys
input = sys.stdin.readline

N = int(input())
original = []
words = []

for i in range(N):
    w = input().rstrip()
    original.append(w)
    words.append((w, i))

words.sort(key=lambda x: x[0])

# 1️. 최대 접두사 길이 찾기
max_len = 0

def lcp(a, b):
    length = 0
    for i in range(min(len(a), len(b))):
        if a[i] == b[i]:
            length += 1
        else:
            break
    return length

for i in range(N - 1):
    if words[i][0] == words[i + 1][0]:
        continue
    cur = lcp(words[i][0], words[i + 1][0])
    max_len = max(max_len, cur)

# 2️. S 찾기
S_idx = None

for i in range(N - 1):
    if words[i][0] == words[i + 1][0]:
        continue
    cur = lcp(words[i][0], words[i + 1][0])
    if cur == max_len:
        candidate = min(words[i][1], words[i + 1][1])
        if S_idx is None or candidate < S_idx:
            S_idx = candidate

# 3️. T 찾기
T_idx = None
S_word = original[S_idx]

for i in range(N):
    if i == S_idx:
        continue
    if original[i] == S_word:
        continue
    if lcp(S_word, original[i]) == max_len:
        if T_idx is None or i < T_idx:
            T_idx = i

print(original[S_idx])
print(original[T_idx])