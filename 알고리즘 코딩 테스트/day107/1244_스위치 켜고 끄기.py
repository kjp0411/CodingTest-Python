# https://www.acmicpc.net/problem/1244
import sys
input = sys.stdin.readline

n_switch = int(input())
switches = list(map(int, input().split()))

n_student = int(input())
students = []   # (gender, num)
for i in range(n_student):
    # (gender)남자: 1, (gender)여자: 2
    gender, num = map(int, input().split())
    students.append((gender, num))

# 학생 순회
for gender, num in students:
    idx = num - 1

    # 남학생 처리
    if gender == 1:
        for i in range(idx, n_switch, num):
            switches[i] ^= 1

    # 여학생 처리
    else:
        left = right = idx
        while left >= 0 and right < n_switch and switches[left] == switches[right]:
            left -= 1
            right += 1

        left += 1
        right -= 1

        for i in range(left, right + 1):
            switches[i] ^= 1

# 출력 처리(20개씩)
for i in range(n_switch):
    print(switches[i], end=' ')
    if (i + 1) % 20 == 0:
        print()