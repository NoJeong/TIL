import sys
import copy
sys.stdin = open('input.txt')


for _ in range(1):
    tc = int(input())
    box = [list(map(int, input().split())) for _ in range(100)]
    j_li = []

    for a in range(100):
        if box[99][a] == 1:
            j_li += [a]
    cnt1 = 100000000
    for j in range(len(j_li)):
        i = 98
        cnt = 0
        box1 = copy.deepcopy(box)
        a = 0
        while i > 0:
            if j_li[j] == 0:
                if box1[i][j_li[j]+1] == 1:
                    cnt += 1
                    box1[i][j_li[j]] = 0
                    j_li[j] += 1
                else:
                    cnt += 1
                    i -= 1
            elif j_li[j] == 99:
                if box1[i][j_li[j]-1] == 1:
                    cnt += 1
                    box1[i][j_li[j]] = 0
                    j_li[j] -= 1
                else:
                    cnt += 1
                    i -= 1
            else:
                if box1[i][j_li[j]-1] == 1:
                    cnt += 1
                    box1[i][j_li[j]] = 0
                    j_li[j] -= 1
                elif box1[i][j_li[j]+1] == 1:
                    cnt += 1
                    box1[i][j_li[j]] = 0
                    j_li[j] += 1
                else:
                    cnt += 1
                    i -= 1
            if cnt < cnt1:
                cnt1 = cnt
                result = j_li[j]
    print("#{} {}".format(tc, result))