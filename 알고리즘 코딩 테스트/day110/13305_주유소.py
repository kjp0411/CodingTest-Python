# https://www.acmicpc.net/problem/13305
N = int(input())
roads = list(map(int, input().split()))
gas_station = list(map(int, input().split()))

total_cost = 0
min_price = gas_station[0]   # 지금까지 본 최소 기름값

for i in range(N - 1):
    if gas_station[i] < min_price:
        min_price = gas_station[i]
    total_cost += min_price * roads[i]

print(total_cost)