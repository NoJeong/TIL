#답
#1 1
#2 4
#3 27
#4 11
#5 42
#6 32
#7 2
#8 3
#9 25
#10 0
import sys
sys.stdin = open('장훈이의 높은선반.txt')

def check(i,n):
    global total,B
    if i==n:
        if B<=sum(people)<total:
            total = sum(people)
    else:
        people.append(base[i])
        check(i+1,n)
        people.pop()
        check(i+1,n)


for tc in range(1, int(input())+1):
    N, B = map(int, input().split())
    base = list(map(int, input().split()))
    people = []
    total=1000000000000
    check(0,N)
    print(f'#{tc} {abs(B-total)}')