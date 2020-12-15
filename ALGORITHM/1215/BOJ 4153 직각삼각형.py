import sys
sys.stdin = open('BOJ 4153 직각삼각형.txt')

while 1:
    base = list(map(int, input().split()))

    if base[0] == 0:
        break

    a = base.pop(base.index(max(base)))
    if a ** 2 == (base[0] ** 2) + (base[1] ** 2):
        print('right')
    else:
        print('wrong')