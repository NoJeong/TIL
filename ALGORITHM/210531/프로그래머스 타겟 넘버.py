import sys
sys.stdin = open('프로그래머스 타겟 넘버.txt')


def solution(numbers, target):
    answer = 0

    def dfs(numbers, target, index):
        nonlocal answer
        if index < len(numbers):
            numbers[index] *= 1
            dfs(numbers, target, index + 1)

            numbers[index] *= -1
            dfs(numbers, target, index + 1)
        elif sum(numbers) == target:
            answer += 1
    dfs(numbers, target, 0)

    return answer


a = list(map(int,input().split()))
b = int(input())

solution(a,b)

