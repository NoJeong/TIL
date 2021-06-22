def solution(m, n, board):
    answer = 0
    boards = [[0] * n for i in range(m)]
    for i in range(m):
        for j in range(n):
            boards[i][j] = board[i][j]

    done = set()
    flag = True
    while flag:
        for i in range(m - 1):
            for j in range(n - 1):
                if boards[i][j] == boards[i][j + 1] == boards[i + 1][j] == boards[i + 1][j + 1] != 0:
                    done.add((i, j))
                    done.add((i, j + 1))
                    done.add((i + 1, j))
                    done.add((i + 1, j + 1))
        if not done:
            flag = False
        while done:
            a, b = done.pop()
            boards[a][b] = 0
            answer += 1

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if boards[i][j] == 0:
                    for a in range(i - 1, -1, -1):
                        if boards[a][j] != 0:
                            boards[i][j], boards[a][j] = boards[a][j], boards[i][j]
                            break
    return answer