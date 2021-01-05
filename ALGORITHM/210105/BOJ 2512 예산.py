import sys
sys.stdin = open('BOJ 2512 예산.txt')

input = sys.stdin.readline
N = int(input())
base = list(map(int,input().split()))
budget = int(input())
l,r = 1, max(base)

while l <= r:
    mid = ((l+r)//2)
    count = 0
    for i in base:
        if i <= mid:
            count += i
        elif i > mid:
            count += mid
    if count > budget:
        r = mid - 1
    elif count <= budget:
        l = mid + 1
print(r)