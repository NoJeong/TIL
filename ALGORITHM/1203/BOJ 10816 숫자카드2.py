import sys
sys.stdin = open('BOJ 10816 숫자카드2.txt')

N = int(input())
base = list(map(str,input().split()))
M = int(input())
hands = list(map(str,input().split()))
base_dict = {}
for i in base:
    if i in base_dict:
        base_dict[i] += 1
    else:
        base_dict[i] = 1

for i in hands:
    if i in base_dict:
        print(base_dict[i], end=' ')
    else:
        print(0,end=' ')