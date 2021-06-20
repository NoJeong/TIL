def solution(n,a,b):
    answer = 0

    flag = True
    while flag:
        answer += 1
        if (a+1)//2 == (b+1)//2:
            flag = False
        a = (a+1)//2
        b = (b+1)//2

    return answer