import sys
sys.stdin = open('boj 직사각형탈출.txt')

x,y,w,h = map(int, input().split())
print(min(x,y,w-x,h-y))