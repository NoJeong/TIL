import sys
sys.stdin = open('별 찍기.txt')

N = int(input())
for i in range(N):
    print('*'*(N-i))