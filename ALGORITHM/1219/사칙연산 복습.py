import sys
sys.stdin = open('사칙연산.txt')

def calculate(i):
    if len(base[i-1]) == 2:
        return int(base[i-1][1])
    else:
        num1 = int(base[i-1].pop())
        num2 = int(base[i-1].pop())
        if base[i-1][1] == '+':
            return calculate(num2) + calculate(num1)
        elif base[i-1][1] == '-':
            return calculate(num2) - calculate(num1)
        elif base[i-1][1] == '*':
            return calculate(num2) * calculate(num1)
        elif base[i-1][1] == '/':
            return calculate(num2) / calculate(num1)


for tc in range(2):
    N = int(input())
    base =[list(input().split()) for _ in range(N)]
    print(calculate(1))
