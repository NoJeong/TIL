# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python 3.6
    S = S.split()
    main_li = list()
    try:
        for i in S:
            if i == '-':
                a = main_li.pop(-1)
                b = main_li.pop(-1)
                if a - b > 0:
                    main_li.append(a - b)
                else:
                    raise Exception
            elif i == '+':
                a = main_li.pop(-1)
                b = main_li.pop(-1)
                main_li.append(abs(a + b))
            elif i == 'DUP':
                main_li.append(main_li[-1])
            elif i == 'POP':
                main_li.pop(-1)
            else:
                main_li.append(int(i))
        return main_li[-1]
    except:
        return -1
