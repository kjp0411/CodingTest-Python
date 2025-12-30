# https://www.acmicpc.net/problem/17266
# 굴다리 모든 길 0~N을 밝히게 가로등 설치
# 설치할 가로등 개수는 M개, 위치는 x
# 각 가로등은 높이만큼 주위를 비출 수 있음
# (단, 가로등의 높이가 높을수록 가격이 비싸짐)
import math

N = int(input())
M = int(input())
x = list(map(int, input().split()))
d = []

# 시작점과 첫번째 가로등의 거리 추출
d.append(x[0])

# index가 붙어 있는 가로등끼리의 거리 추출 (단, 이 경우는 거리/2 로 계산해야됨)
# 총 가로등이 5개라면 구해야하는것은 1~2, 2~3, 3~4, 4~5 총 4개
for i in range(M-1):
    dist = (x[i+1] - x[i]) / 2
    d.append(math.ceil(dist))

# 종점과 마지막 가로등의 거리 추출
d.append(N - x[-1])

# max값 출력
print(max(d))