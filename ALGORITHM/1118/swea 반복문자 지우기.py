import sys
sys.stdin = open('input.txt')

T = int(input())
#한개씩 스택에 쌓는다
#스택에서 마지막인덱스와 그 전 인덱스를 비교한다
# 같으면 지운다

for tc in range(1,T+1):
    stack = list()
    base = input()
    for i in range(len(base)):
        stack.append(base[i])
        if len(stack) >= 2 and stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()
    print('#{} {}'.format(tc, len(stack)))








# for tc in range(1,T+1):
#     base = input()
#     stack = list()
#     for i in range(len(base)-1):
#         if i+1 == len(base):
#             if base[i] != base[i+1]:
#                 stack.append(base[i+1])
#         if base[i] != base[i + 1]:
#             if base[i] == base[i-1]:
#                 if base[i] == base[i-1] == base[i-2]:
#                     stack.append((base[i]))
#                 continue
#             else:
#                 stack.append(base[i])
#         else:
#             continue
#
#     print(stack)
