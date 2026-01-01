# https://www.acmicpc.net/problem/20920
# 단어장 단어 순서(우선 순위)
# 1. 자주 나오는 단어일수록 앞에 배치한다.
# 2. 해당 단어의 길이가 길수록 앞에 배치한다.
# 3. 알파벳 사전 순으로 앞에 있는 단어일수록 앞에 배치한다.
# M보다 짧은 길이의 단어는 읽는 것만으로도 암기 가능 -> 길이가 M 이상인 단어들만 적용
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
freq = {}

# 길이가 M 이상인 단어들만 count
for _ in range(N):
    word = input().strip()
    if len(word) < M:
        continue
    freq[word] = freq.get(word, 0) + 1

# 정렬
words = sorted(
    freq.items(),
    key=lambda x: (-x[1], -len(x[0]), x[0])
)

for word, _ in words:
    print(word)