from itertools import permutations
import math


def solution(numbers):
    answer = set()

    for i in range(1, len(numbers) + 1):
        tmp_list = list(map(''.join, list(permutations(numbers, i))))
        tmp_list = list(set(map(int, tmp_list)))
        print(tmp_list)
        for i in range(len(tmp_list)):
            flag = False
            if tmp_list[i] < 2:
                continue
            for j in range(2, int(math.sqrt(tmp_list[i])) + 1):
                if tmp_list[i] % j == 0:
                    flag = True
            if not flag:
                answer.add(tmp_list[i])

    return len(answer)


이렇게