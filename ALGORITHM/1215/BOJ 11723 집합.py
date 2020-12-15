import sys
sys.stdin = open('BOJ 11723 집합.txt')


S = set()
for tc in range(1,int(input())+1):
    base = list(map(str,input().split()))
    if len(base) == 1:
        S.add('1')
    if base[0] == 'add':
        S.add(base[1])
    elif base[0] == 'remove':
        S.remove(base[1])
    elif base[0] == 'check':
        if base[1] in S:
            print(1)
        else:
            print(0)
    elif base[0] == 'toggle':
        if base[1] in S:
            S.remove(base[1])
        else:
            S.add(base[1])
    elif base[0] == 'all':
        S = set()
        for i in range(1,21):
            S.add(str(i))

    elif base[0] == 'empty':
        S.clear()

