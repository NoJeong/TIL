import math, sys
sys.stdin = open('BOJ 1010 다리놓기.txt')

for _ in range(int(input())):
    a,b = map(int, input().split())
    c = math.factorial(b-a)
    b = math.factorial(b)
    a = math.factorial(a)
    print(b//(a*c))