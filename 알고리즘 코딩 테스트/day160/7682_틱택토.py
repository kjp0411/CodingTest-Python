# https://www.acmicpc.net/problem/7682
def win(board, ch):
    #가로 완성
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == ch:
            return True

    #세로 완성
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] == ch:
            return True

    # 대각선 완성
    if board[0][0] == board[1][1] == board[2][2] == ch:
        return True

    if board[0][2] == board[1][1] == board[2][0] == ch:
        return True

    return False

while True:
    X_count = 0
    O_count = 0

    S = input().strip()
    if S == 'end':
        break
    board = [S[0:3], S[3:6], S[6:9]]

    for ch in S:
        if ch == 'X':
            X_count += 1
        elif ch == 'O':
            O_count += 1
        else:
            continue

    # 1단계: 개수 판정
    if not (X_count == O_count or X_count == O_count + 1):
        print("invalid")
        continue

    # 2단계: 승리 판정
    X_win = win(board, 'X')
    O_win = win(board, 'O')

    # 3단계: 조합 판정
    if X_win and O_win:     # 우승자가 2명인 경우(존재 X)
        print("invalid")
    elif X_win:             # 우승자가 X이며 개수 판단
        if X_count == O_count + 1:
            print("valid")
        else:
            print("invalid")
    elif O_win:             # 우승자가 O이며 개수 판단
        if X_count == O_count:
            print("valid")
        else:
            print("invalid")
    else:                   # 우승자가 없는 경우 판단
        if X_count + O_count == 9:
            print("valid")
        else:
            print("invalid")