for i in range(3):
    print('hello')

#재귀 호출로 단순 반복을 구현

#재귀 호출이 몇번 행해졌는지는 알 수 있어야한다.

#재귀 호출의 종료는 매개변수를 기준으로 판단한다.


def printHello(i): # i를 이용해서 종료를 판단
    if i == 3:      #기저사례
        pass
    else:           #유도사례
        print('Hello')
        printHello(i + 1)

printHello(0)


def printHello(i, n): # i를 이용해서 종료를 판단
    if i == n:      #기저사례
        pass
    else:           #유도사례
        print(i, '> Hello')
        printHello(i + 1, n)
        print(i, '> Hello')
printHello(0, 3)

def printHello(i, n): # i를 이용해서 종료를 판단
    if i == n:      #기저사례
        print(arr)
    else:           #유도사례
        arr[i] = i + 1
        printHello(i + 1, n)
        arr[i] = 0


N = 3
arr = [0] * N
printHello(0, N)
print(arr)

cnt = 0
def printHello(i, n):  # i를 이용해서 종료를 판단
    if i == n:
        global cnt; cnt += 1
    else:
        printHello(i + 1, n)
        printHello(i + 1, n)

N = 3
printHello(0, N)
print(cnt)



cnt = 0
def printHello(i, n):  # i를 이용해서 종료를 판단
    if i == n:
        global cnt; cnt += 1
        print(bits)
    else:
        bits[i] = 1
        printHello(i + 1, n)
        bits[i] = 0
        printHello(i + 1, n)

bits = [0] * 3
N = 3
printHello(0, N)
print(cnt)


arr = 'ABC'
bits = []
for i in range(2):
    bits.append(i)

    for i in range(2):
        bits.append(i)

        for i in range(2):
            bits.append(i)
            print(bits)
bits=[1]*3
def subset(k, n):
    if k ==n:
        print(">",bits)
    else:
        # for i in range(2):
        bits[k] = 0
        subset(k+1, n)
        bits[k] = 1
        subset(k + 1, n)

subset(0, 3)



arr = 'ABC'
bits = []
def subset(k, n):
    if k ==n:
        print(">>",bits)
    else:
        # for i in range(2):
        bits.append(arr[k])
        subset(k+1, n)
        bits.pop()
        subset(k + 1, n)

subset(0, 3)