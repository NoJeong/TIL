import sys
from collections import deque
sys.stdin = open('junglebook.txt')
def minimumGroups(predators):
    start_list = []
    for i in range(len(predators)):
        if predators[i] == -1:
            start_list.append(i)
    final = 0
    for i in start_list:
        if final < result:
            final = result
    stack = [predator]
    cnt = 1

    while 1:
        if len(stack) == 0:
            break
        animal = stack.pop()
        for i in range(len(predators)):
            if animal == predators[i]:
                cnt += 1
                stack.append(i)
    return cnt





predators_count = int(input().strip())

predators = []

for _ in range(predators_count):
    predators_item = int(input().strip())
    predators.append(predators_item)

    result = minimumGroups(predators)

print(result)