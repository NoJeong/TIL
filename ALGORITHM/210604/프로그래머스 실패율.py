def solution(N, stages):
    answer = []
    temp_li = []
    base = len(stages)
    for i in range(1, N + 1):
        a = stages.count(i)
        if not base:
            temp_li.append((i, 0))
        elif a == 0:
            temp_li.append((i, 0))
        else:
            temp_li.append((i, a / base))

        base -= a
    temp_li.sort(key=lambda x: (-x[1], x[0]))
    print(temp_li)
    for i in temp_li:
        answer.append(i[0])

    return answer