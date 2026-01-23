# https://www.acmicpc.net/problem/1283
N = int(input().strip())
used = []

for _ in range(N):
    selected_idx = -1
    found = False
    line = input()

    for i in range(len(line)):
        if i == 0:
            if line[i].lower() not in used:
                selected_idx = i
                used.append(line[i].lower())
                found = True
                break

        elif i > 0 and line[i-1] == ' ':
            if line[i].lower() not in used:
                selected_idx = i
                used.append(line[i].lower())
                found = True
                break

    for j in range(len(line)):
        if line[j].lower() not in used and found == False and line[j].isalpha():
            selected_idx = j
            used.append(line[j].lower())
            break

    if selected_idx == -1:
        print(line)
    else:
        print(line[:selected_idx]
        + "[" + line[selected_idx] + "]"
        + line[selected_idx+1:])