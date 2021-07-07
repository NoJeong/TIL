import sys, math

sys.stdin = open('백준 Z.txt')

def find(size, b, c):
    global answer
    #처음숫자 = > size, quadrant
    target = (b+1)*(c+1)
    quadrant = target % 4**(size - 1)
    print(target, quadrant, answer, size)

    if quadrant == 0:
        quadrant = target // 4**(size - 1)
    if quadrant == 0:
        answer += 4 ** (size - 1) * 3
    elif quadrant == 1:
        pass
    else:
        answer += 4 ** (size - 1) * (quadrant)

    #처음숫자 = 처음숫자 - 2 ** (size - 1) * quadrant
    target = target - (2**(size-1) * (quadrant+1))
    if target < 4:
        answer += quadrant
        return
    #1사분면 = > 가만히
    if quadrant == 1:
        find(size - 1, b, c)
    #2사분면 = > c - 2 ** (size - 1)
    elif quadrant == 2:
        find(size - 1, b, c - 2 ** (size - 1))
    #3사분면 = > b - 2 ** (size - 1)
    elif quadrant == 3:
        find(size - 1, b - 2 ** (size - 1), c)
    #4사분면 = > c - 2 ** (size - 1), b - 2 ** (size - 1)
    else:
        find(size - 1, b - 2 ** (size - 1), c - 2 ** (size - 1))

a, b, c = map(int, input().split())
answer = 0
find(a,b,c)
print(answer)
