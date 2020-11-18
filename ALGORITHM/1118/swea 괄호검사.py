import sys
sys.stdin = open('input.txt')

def check(arr):
    for i in range(len(arr)):
        if arr[i] == '(' or arr[i] == '[' or arr[i] == '{': # push
          stack.append(arr[i])
        elif arr[i] == ')' or arr[i] == ']' or arr[i] == '}': #pop하고 비교해야
            if len(stack) == 0:
                return 0
            else:
                tmp = stack.pop() #비어있지 않으면 pop하고, 짝이 맞는지 검사해야한다.
                if arr[i] ==')' and tmp == '(':
                    continue
                elif arr[i] ==']' and tmp == '[':
                    continue
                elif arr[i] =='}' and tmp == '{':
                    continue
                ###여기 까지 진입하면 스택은 비어있지 않은데 짝이 맞지 않다.
                else:
                    return 0

    if stack:
        return 0
    else:
        return 1
T = int(input())
for tc in range(1, T+1):
    stack = []
    arr = input()
    print('#{} {}'.format(tc, check(arr)))