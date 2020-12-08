import sys
sys.stdin = open('BOJ 11050 이항계수1.txt')

def go(n,k):

    if n == k:
        return 1
    elif k == 0:
        return 1
    else:
        return go(n-1,k-1) + go(n-1,k)



N,K = map(int, input().split())


print(go(N,K))