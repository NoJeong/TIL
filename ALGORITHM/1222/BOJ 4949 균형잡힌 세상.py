import sys
sys.stdin = open('BOJ 4949 균형잡힌 세상.txt')

while 1:
    base = list(input())
    if len(base) == 1:
        break
    stack = []
    for i in base:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if not stack:
                print('no')
                break
            if stack[-1] == '(':
                stack.pop()
            else:
                print('no')
                break
        elif i == ']':
            if not stack:
                print('no')
                break
            if stack[-1] == '[':
                stack.pop()
            else:
                print('no')
                break

        elif i == '.' and not stack:
            print('yes')
        elif i == '.' and stack:
            print('no')

