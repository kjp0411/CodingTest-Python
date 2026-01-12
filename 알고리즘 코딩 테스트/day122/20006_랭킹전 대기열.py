# https://www.acmicpc.net/problem/20006
# 매칭 시스템
# 1. 플레이어가 입장을 신청하였을 때 매칭이 가능한 방이 없다면 새로운 방을 생성하고 입장시킨다.
# (이때 해당 방에는 처음 입장한 플레이어의 레벨을 기준으로 -10부터 +10까지 입장 가능하다.)
# 2. 입장 가능한 방이 있다면 입장시킨 후 방의 정원이 모두 찰 때까지 대기시킨다.
# (이때 입장이 가능한 방이 여러 개라면 먼저 생성된 방에 입장한다.)
# 3. 방의 정원이 모두 차면 게임을 시작시킨다.
P, M = map(int, input().strip().split())
players = []
for i in range(P):
    p_level, p_id = input().strip().split()
    p_level = int(p_level)
    players.append((p_level, p_id))

rooms = []
# 그 방에 처음 들어온 플레이어의 레벨을 기준으로 방을 생성
for p_level, p_id in players:
    p_input = False
    for room in rooms:
        if p_level <= room[0] + 10 and p_level >= room[0] - 10 and len(room[1]) < M:
            p_input = True
            room[1].append((p_level, p_id))
            break
    if p_input == False:
        room = [p_level, [(p_level, p_id)]]
        rooms.append(room)

# 출력
for room in rooms:
    room[1].sort(key=lambda x: x[1])  # 사전순으로 정렬

    if len(room[1]) == M:
        print("Started!")
        for l, i in room[1]:
            print(l, i)
    else:
        print("Waiting!")
        for l, i in room[1]:
            print(l, i)