# https://www.acmicpc.net/problem/2816
# 채널 리스트를 조절해 KBS1을 첫 번째, KBS2를 두 번째로 만들기
# 티비를 켜면 시청 가능한 채널 리스트를 보여줌
# 리스트 왼편에는 작은 화살표(cursur)가 있음: 현재 선택한 채널(첫 번째 채널이 디폴트)
# 1번 버튼: 화살표를 한 칸 아래로 내린다.(채널 1번이면 2번으로 변경)
# 2번 버튼: 화살표를 위로 한 칸 올린다.(채널 2번이면 1번으로 변경)
# 3번 버튼: 현재 선택한 채널을 한 칸 아래로 내린다.(채널 1번과 2번의 위치를 바꾼다) 화살표는 2번
# 4번 버튼: 현재 선택한 채널을 위로 한 칸 올린다(채널 2번과 1번 위치를 바꾼다.) 화살표는 1번
# 화살표가 채널 리스트의 범위를 벗어나면 명령 무시
N = int(input())
channels = [input().strip() for _ in range(N)]

cursor = 0
answer = []

# KBS1을 0번으로
while channels[0] != "KBS1":
    # KBS1 위치로 커서 이동
    if channels[cursor] != "KBS1":
        cursor += 1
        answer.append('1')
    else:
        # 한 칸 위로 올리기 (swap)
        channels[cursor], channels[cursor-1] = channels[cursor-1], channels[cursor]
        cursor -= 1
        answer.append('4')

# KBS2를 1번으로
while channels[1] != "KBS2":
    if channels[cursor] != "KBS2":
        cursor += 1
        answer.append('1')
    else:
        channels[cursor], channels[cursor-1] = channels[cursor-1], channels[cursor]
        cursor -= 1
        answer.append('4')

print(''.join(answer))