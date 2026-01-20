# https://www.acmicpc.net/problem/2531
N, D, K, C = map(int, input().strip().split())
sushi_type = []
for _ in range(N):
    sushi_type.append(int(input().strip()))
sushi_type = sushi_type + sushi_type[0:K-1]

sushi_count = {}
for i in range(K):
    if sushi_type[i] not in sushi_count:
        sushi_count[sushi_type[i]] = 1
    else:
        sushi_count[sushi_type[i]] += 1

l = 0
max_type = 0
if C not in sushi_count:
    max_type = len(sushi_count) + 1

for l in range(1, N):
    r = l + K - 1
    sushi_count[sushi_type[l-1]] -= 1
    if sushi_count[sushi_type[l-1]] == 0:
        sushi_count.pop(sushi_type[l-1])

    if sushi_type[r] not in sushi_count:
        sushi_count[sushi_type[r]] = 1
    else:
        sushi_count[sushi_type[r]] += 1
    current_type = len(sushi_count)
    if C not in sushi_count:
        current_type += 1
        if current_type > max_type:
            max_type = current_type
    else:
        if current_type > max_type:
            max_type = current_type

print(max_type)