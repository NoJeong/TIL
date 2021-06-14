def solution(number, k):
    answer = []
    cnt = 0
    for i in number:
        while answer and i > answer[-1] and cnt < k:
            answer.pop(-1)
            cnt+= 1

        answer.append(i)
    while cnt < k:
        answer.pop(-1)
        cnt += 1
    return ''.join(answer)