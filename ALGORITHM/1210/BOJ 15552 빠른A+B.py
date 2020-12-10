import sys
sys.stdin = open('BOJ 15552 빠른A+B.txt')

for i in range(int(input())):
    a,b = map(int, sys.stdin.readline().split())
    print(a+b)