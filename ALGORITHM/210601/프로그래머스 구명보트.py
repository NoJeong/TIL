def solution(people, limit):
    answer = 0
    people = sorted(people)
    max_cnt = -1
    min_cnt = 0
    while (len(people) + max_cnt) >= min_cnt:
        answer += 1
        min_num = people[min_cnt]
        max_num = people[max_cnt]
        if (min_num + max_num) <= limit:
            min_cnt += 1
        max_cnt -= 1
    return answer