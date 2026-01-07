# https://www.acmicpc.net/problem/2607
# 같은 구성
# 다른 구성 + (한 문자 더하기 or 빼기)-> 비슷한 구성
# 같은 길이에서 한 문자 만 교체
# 비슷한 단어 출력
def alphabet_count(word):
    alphabet = [0] * 26
    for ch in word:
        idx = ord(ch) - ord('A')
        alphabet[idx] += 1
    return alphabet

N = int(input())
first_word = input()
compare = []

base = alphabet_count(first_word)
count = 0
for i in range(N-1):
    word = input()
    compare = alphabet_count(word)
    diff = 0
    for j in range(26):
        diff += abs(base[j] - compare[j])

    if abs(len(first_word) - len(word)) == 0 and diff == 0:
        count += 1
    elif abs(len(first_word) - len(word)) == 0 or abs(len(first_word) - len(word)) == 1:
        if diff == 1 or diff == 2:
            count += 1

print(count)