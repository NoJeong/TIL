import sys
sys.stdin = open('BOJ 11866 요세푸스 문제0.txt')

N,K = map(int,input().split())
base = list(range(1,N+1))
stack = list()
num = 0
while base:
    num += K-1
    if num >= len(base):
        num = num % len(base)

    stack.append(str(base.pop(num)))

print('<',', '.join(stack),'>',sep='')