# https://www.acmicpc.net/problem/14658
N, M, L, K = map(int, input().split())
stars = []

for _ in range(K):
    x, y = map(int, input().split())
    stars.append((x, y))

# 후보
xs = [x for x, y in stars]
ys = [y for x, y in stars]

best_count = 0
for sx in xs:
    for sy in ys:
        count = 0
        for x, y in stars:
            if sx <= x <= sx + L and sy <= y <= sy + L:
                count += 1

        best_count = max(best_count, count)
print(K - best_count)