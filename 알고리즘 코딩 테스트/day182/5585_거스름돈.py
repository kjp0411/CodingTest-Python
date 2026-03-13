# https://www.acmicpc.net/problem/5585
N = int(input())
amount = 1000 - N
coins = [500, 100, 50, 10, 5, 1]

count = 0

for coin in coins:
    count += amount // coin
    amount %= coin

print(count)