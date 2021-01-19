import sys
sys.stdin = open('별 찍기.txt')

N = int(input())
for i in range(1,N+1):
    print(' '*((2*N-(2*i-1))//2) + '*'*(2*i-1))
