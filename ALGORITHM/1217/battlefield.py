import sys
sys.stdin = open('battlefield')

dc = [0, 0, 1, -1]
dr = [1, -1, 0, 0] # 우좌하상


for tc in range(int(input())+1):
    H, W = map(int, input().split())
    field = [input() for _ in range(H)]
    N =int(input())
    command = input()
    tank = ['<', '>', '^', 'v']
    #tank
    for i in range(H):
        for j in range(W):
            if field[i][j] == '<' or '>' or '^' or 'v':
                y = i
                x = j
                if field[i][j] == '<':
                    tank = '<'
                elif field[i][j] == '>':
                    tank = '>'
                elif field[i][j] == '^':
                    tank = '^'
                else:
                    tank = 'v'
    #조작
    for n in range(N):
        if command[n] == 'U':
            tank = '^'
            y += dc[3]
        elif command[n] == 'D':
            tank = 'v'
            y += dc[2]
        elif command[n] == 'L':
            tank = '<'
            x += dr[1]
        elif command[n] == 'R':
            tank = '>'
            x += dr[0]
        else: #"S"
            if tank == '^':
                while 1:
                    y += dc[3]
                    if field[y][x] == '*':
                        field[y][x] == '.'
                        break
                    elif field[y][x] == '#':
                        break
                    else:
                        continue