import sys
sys.stdin = open('피보나치 수.txt')

N = int(input())

def fibo(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    return fibo(n-1) + fibo(n-2)

result = fibo(N)
print(result)