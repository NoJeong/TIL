import sys
sys.stdin = open('별 찍기.txt')

N = int(input())
for i in range(1,N+1):
    print('*'*i + ' '*(2(i-1)) + '*'*i)
for i in range(1,N+1):
    print('*'*(N-i) + ' '*(2*i) + '*'*(N-i))
