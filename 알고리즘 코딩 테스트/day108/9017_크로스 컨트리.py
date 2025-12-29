# https://www.acmicpc.net/problem/9017
# 한 팀은 6명의 선수(팀 점수: 상위 4명만 계산)
# 점수는 자격을 갖춘 팀의 주자들에게만 주어짐(6명의 주자가 참가하지 못한 팀은 제외)
# 결승점을 통과한 순서대로 점수를 받고, 점수를 더하여 가장 낮은 점수를 얻는 팀이 우승
# (동점의 경우에는 다섯 번째 주자가 가장 빨리 들어온 팀이 우승)
from collections import defaultdict

T = int(input())

for i in range(T):
    N = int(input())
    D = list(map(int, input().split()))

    team_count = defaultdict(int)
    for team in D:
        team_count[team] += 1

    # 자격이 있는 팀
    valid_teams = set(team for team, cnt in team_count.items() if cnt == 6)

    scores = defaultdict(list)
    score = 1

    # 점수 부여
    for team in D:
        if team in valid_teams:
            scores[team].append(score)
            score += 1

    # 팀 점수 계산
    result = []
    for team in scores:
        total = sum(scores[team][:4])
        fifth = scores[team][4]
        result.append((total, fifth, team))

    # 우승 팀 결정
    result.sort()
    print(result[0][2])