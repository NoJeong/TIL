import sys
sys.stdin = open('BOJ 1463 1로만들기.txt')

def calc(n,cnt):
    global ct
    if cnt > ct:
        return

    if n == 1:
        if ct > cnt:
            ct = cnt
        return cnt

    if not n % 2:
        calc(n//2,cnt+1)
        calc(n-1, cnt+1)
        if not n % 3:
            calc(n//3,cnt+1)
    elif not n % 3:
        calc(n//3,cnt+1)
        calc(n-1,cnt+1)
        if not n % 2:
            calc(n // 2, cnt + 1)
    else:
        calc(n-1,cnt+1)

N = int(input())
ct = N
result = calc(N,0)
print(ct)