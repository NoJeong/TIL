# 알고리즘 문제 후기

### SWEA 4831.



#### 내코드



```python
a = int(input())
for p in range(a):
    count = 0
    stop = 0
    k, n, m = map(int,input().split())
    b = list(map(int,input().split()))
    for i in range(0, len(b)-1):
        if b[0] < k and b[1] <= k:
            i += 1

        if stop + k >= b[i]:
            try:
                if stop + k >= b[i + 1]:
                    stop = b[i+1]
                    count += 1
                else:
                    stop = b[i]
                    count += 1
            except:
                continue
        else:
            count = 0
            break


    print(f'#{p+1} {count}')
```

* 이건 오답이다.
* 나는 0에서 출발해서 다음 정류소를 탐색한 다음, 그 다음 정류소를 갈 수 있는지도 탐색하는 알고리즘을 만들었다.
* 그렇게 해서 갈 수 있으면 한 정류소를 뛰어넘어가고, 그렇지 않으면 다음 정류소에 도착하게끔했다.
* 근데 문제는 이러한 로직은 예시문에서는 정답이 나오지만 임의의 파일을 돌렸을때는 에러가 났다.
* 에러가 왜 나는지 분석해봤는데 보기는 `1,3,5,7,9` 이렇게 띄엄띄엄 나오지만
* 만약 `1, 2, 3, 4, 5` 와같이 배치 되어있을때 5만큼 갈 수 있는 버스가 한번에 5를 가지못하기 때문이다.
* 나는 끝내 해결하지 못했다.

```python
a = int(input())

for p in range(a):
    count = 0
    stop = 0
    arrive = True
    k, n, m = map(int,input().split())
    b = list(map(int,input().split()))

    for i in range(0, len(b)-1):
        if b[i+1] - b[i] > k:
            count = 0
            arrive = False

    if arrive == True:
        while stop < n - k:
            for i in range(k):
                if stop+k-i in b:
                    count += 1
                    stop = stop+k-i
                    break



    print(f'#{p+1} {count}')
```

---

* 이 코드는 내코드는 아니다
* 하지만 정말 간단한 알고리즘으로 짠것같아서 내가 참고했다
* 다음번엔 이런일이 발생하지 않도록 해야겠다.
* 이 코드는 정류소의 간격을 보고 갈 수 없는 길은  `Fail`을 줘버려서 논외로 친다.
* 그리고 하이라이트는 내가 막혔던 부분을 정말 쉽게 해결했는데 바로 갈수있을만큼 가고 거기서부터 역으로 정류소를 탐색하는 것이었다.
* 이렇게되면 그 앞에 정류소가 몇개가 있는지 상관하지 않아도 된다.
* 유레카이자 현타였다.
* 이제 코드 짤때는 생각의 틀에서 벗어나도록 많이 노력해야겠다.