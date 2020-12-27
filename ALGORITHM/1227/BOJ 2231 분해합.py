N = int(input())

n = 1
while 1:
    base = 0
    base += n
    n = str(n)
    for i in n:
        base += int(i)
    n = int(n)
    if base == N:
        print(n)
        break
    if n == N:
        print(0)
        break
    n += 1
