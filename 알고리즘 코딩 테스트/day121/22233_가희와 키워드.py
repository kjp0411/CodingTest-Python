# https://www.acmicpc.net/problem/22233
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
keywords = set()
for _ in range(N):
    keyword = input().strip()
    keywords.add(keyword)

for _ in range(M):
    blog_keywords = input().strip().split(',')
    for k in blog_keywords:
        if k in keywords:
            keywords.discard(k)

    print(len(keywords))