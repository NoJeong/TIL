def solution(numbers):
    answer = ''
    numbers = list(map(str,numbers))
    numbers.sort(key= lambda x:x*3, reverse=True)
    for j in range(len(numbers)):
        answer += numbers[j]
    if answer[0] == '0':
        answer = '0'
    return answer



def solution(numbers):
    numbers = list(map(str,numbers))
    numbers.sort(key= lambda x:x*3, reverse=True)
    answer = str(int(''.join(numbers)))
    return answer