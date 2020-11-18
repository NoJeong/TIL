import sys
sys.stdin = open('input.txt')

def paper(size):
    if size ==0:
        return 1
    elif size < 0:
        return 0
    return paper(size-10) + paper(size-20)*2



T = int(input())
for tc in range(T):
    n = int(input())
    print('#{} {}'.format(tc+1, paper(n)))