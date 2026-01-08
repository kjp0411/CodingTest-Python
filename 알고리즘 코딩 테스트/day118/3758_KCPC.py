# https://www.acmicpc.net/problem/3758
# 총 K개의 문제를 푼다.
# 문제를 풀고 서버에 제출하면 0 ~ 100점 사이의 점수를 얻는다.
# 풀이를 제출한 팀의 ID, 문제 번호, 점수가 서버의 로그에 제출되는 시간 순서대로 저장된다.
# 풀이는 여러 번 제출할 수 있고, 그 중 최고 점수가 최종 점수다.(한 번도 제출 안하면 0점)
# 팀의 최종 점수는 각 문제에 대해 받은 점수의 총합이다.
# 점수가 동일한 팀이 있다면
# 1. 최종 점수가 같은 경우, 풀이를 제출한 횟수가 적은 팀의 순위가 높다.
# 2. 최종 점수도 같고 제출 횟수도 같은 경우, 마지막 제출 시간이 더 빠른 팀의 순위가 높다.
# 동시에 제출되는 풀이는 없고, 모든 팀이 적어도 한 번은 풀이를 제출한다고 가정하라.
T = int(input())    # 테스트 데이터의 수
for _ in range(T):
    team_list = [[]]
    team_info_list = []
    n, k, t, m = map(int, input().split())  # n: 팀의 개수, k: 문제의 개수, t: 당신 팀의 ID, m: 로그 엔트리의 개수

    for _ in range(n):
        team = [[0] * k, 0, 0]
        team_list.append(team)

    for c in range(m):
        i, j, s = map(int, input().split()) # i: 팀 ID, j: 문제 번호, s: 획득한 점수
        team_list[i][1] += 1
        team_list[i][2] = c+1
        if team_list[i][0][j-1] < s:
            team_list[i][0][j-1] = s

    for i in range(1, len(team_list)):
        team_info = (i, sum(team_list[i][0]), team_list[i][1], team_list[i][2])
        team_info_list.append(team_info)
    team_info_list.sort(key=lambda x: (-x[1], x[2], x[3]))

    for i in range(n):
        if team_info_list[i][0] == t:
            print(i+1)
