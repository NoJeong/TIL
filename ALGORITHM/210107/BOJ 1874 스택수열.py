import sys
sys.stdin = open('BOJ 1874 스택수열.txt')
from collections import deque
N =int(input())
base = [i for i in range(1,N+1)]
search = deque()
for i in range(N):
    search.append(int(input()))
stack = []
result = []
final = []
for i in base:
    if not stack or stack[-1] != search[0]:
        final.append('+')
        stack.append(i)
    if stack and stack[-1] == search[0]:
        while stack and stack[-1] == search[0]:
            final.append('-')
            stack.pop(-1)
            result.append(search.popleft())

if stack:
    print("NO")
else:
    for i in final:
        print(i)