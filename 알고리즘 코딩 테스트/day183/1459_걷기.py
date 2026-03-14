# https://www.acmicpc.net/problem/1459
X, Y, W, S = map(int, input().split())
diag = min(X, Y)
remain = abs(X - Y)

# 1. 직선만 사용
cost1 = (X + Y) * W

# 2. 대각선 최대 사용 + 직선 이동
cost2 = diag * S + remain * W

# 3. 대각선만 사용
if (X + Y) % 2 == 0:
    cost3 = max(X, Y) * S
else:
    cost3 = (max(X, Y) - 1) * S + W

# 4. 대각선 최대 + 남은 거리도 대각선
# 남은 거리 처리
if remain % 2 == 0:
    cost4 = diag * S + remain * S
else:
    cost4 = diag * S + (remain - 1) * S + W

print(min(cost1, cost2, cost3, cost4))