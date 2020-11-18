import sys
import copy
sys.stdin = open('input.txt')


for tc in range(1, 11):
    T = int(input())
    ladders = [list(map(int, input().split())) for _ in range(100)]
    min_cnt = 10000000000
    min_dr = 0
    startings = [i for i in range(100) if ladders[0][i]]
    for starting in startings:
        dc = 0
        dr = starting
        cnt = 0
        while dc < 99:
            dc += 1
            cnt += 1
            if dr > 0 and ladders[dc][dr - 1] == 1:
                while dr > 0 and ladders[dc][dr - 1] == 1:
                    dr -= 1
                    cnt += 1
            elif dr < 99 and ladders[dc][dr + 1] == 1:
                while dr < 99 and ladders[dc][dr + 1] == 1:
                    dr += 1
                    cnt += 1
        if cnt < min_cnt:
            min_dr = starting
            min_cnt = cnt
        print(cnt)
    print('#{} {}'.format(T, min_dr))