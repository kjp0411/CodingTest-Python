# https://www.acmicpc.net/problem/14889
# 축구를 하기 위해 모인 사람의 수는 N 명(N은 무조건 짝수이다.)
# N/2명으로 이루어진 스타트 팀과 링크 팀으로 사람을 나눠야 한다.
from itertools import combinations
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

answer = 1e9
people = range(N)

for team in combinations(people, N//2):
    start = set(team)
    link = set(people) - start

    s1 = s2 = 0

    for i in start:
        for j in start:
            s1 += board[i][j]

    for i in link:
        for j in link:
            s2 += board[i][j]

    answer = min(answer, abs(s1 - s2))

print(answer)