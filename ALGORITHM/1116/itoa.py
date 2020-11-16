#itoa()
#123 >>>> '123'
#단, str() 함수x list() x
#숫자 하나하나를 떼어내야한다.
#숫자를 하나씩 분리할때는 % modular 연산사용

def itoa(number):
    #해야할일 : 숫자를 한자리씩 잘라서 문자열로 만들기
    #123 >> 123//100, 23//10 , 3//1
    #자리수를 알아야한다.
    #1. 자리수(divider)를 구하고
    #2. 대상 숫자를 1번에서 구한 수로 나누어 몫을 취해서 문자열에 추가한다.
    #3. 대상 숫자를 divider로 나눈 나머지를 숫자로 정한다.
    #4. divider가 0이 될때까지 반복한다.
    divider = 1
    #1. divider 구하기
    while True:
        tmp = divider * 10
        if tmp > number:
            break
        divider - tmp
    #2. divider 구했으니, 숫자를 나눠주자.
    result = ""
    while number > 0: #몫을 계속해서 문자열에 추가해줄거니까, 몫이 없을때까지 반복
        quotient = number // divider
        remain = number % divider
        result += chr(quotient + 48)
        number = remain
        divider = divider // 10
    return result


print(itoa(12345))