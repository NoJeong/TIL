# 시험대비 시험에 나올만한 문제 정리

* 가로로 숫자 출력하기

```python
N = int(input())

result = ''
for n in range(1, N+1):
    result += f'{n}' + ' '
    print(result)
```



* 숫자탑쌓기

```python
for n in range(1, N+1):
    for i in range(1, n+1):
        print(i, end=' ')
    print()

```



* 구구단을 외자~!

```python
for n in range(2,N+1):
    print('----[{} 단]----'.format(n))
    for m in range(1,10):

        print('{a} X {b} = {c}'.format(a=n,b=m,c=n*m) )
```

