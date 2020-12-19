import sys
sys.stdin = open('단순2진암호코드.txt')


dic = {'0001101': 0,
       '0011001': 1,
       '0010011': 2,
       '0111101': 3,
       '0100011': 4,
       '0110001': 5,
       '0101111': 6,
       '0111011': 7,
       '0110111': 8,
       '0001011': 9,
       }


for tc in range(1,int(input())+1):
    N, M = map(int, input().split())
    base = [list(input()) for _ in range(N)]
    x = y = 0

    for i in range(N):
        for j in range((M-1),-1,-1):
            if base[i][j] == '1':
                y = i
                x = j
                break
        if base[i][j] == '1':
            y = i
            x = j
            break
    hole = []
    zzak = []
    cnt = 0
    for i in range(8):
        cnt += 1
        temp = ''
        temp_list = base[y][x-7-(7*i)+1:x-(7*i)+1]
        for j in range(len(temp_list)):
            temp += temp_list[j]
        if cnt % 2:
            zzak.append(dic[temp])
        else:
            hole.append(dic[temp])

    seven = (sum(hole)*3) + sum(zzak)
    code = 10 - (seven % 10)

    if code == 10:
        print(f'#{tc} {sum(zzak) + sum(hole)}')
    else:
        print(f'#{tc} 0')