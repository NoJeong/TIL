import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    li = []
    base = input()
    card = {'S':13,'D':13,'H':13,'C':13}
    for i in range(len(base)//3):
       li.append(base[i*3:i*3+3])
    if len(set(li)) != len(li):
        print('#{} ERROR'.format(tc))
    else:
        for i in range(len(li)):
            card[li[i][0]] -= 1
        print('#{} '.format(tc),end='')
        print(*card.values())