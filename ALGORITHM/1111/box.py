boxes = [7,4,2,0,0,6,0,7,0]

# 상자로 채워진 방이있다.
# 방을 오른쪽으로 90도 회전 시켰을 때,
# 낙차가 가장 큰 상자의 낙차를 구하여라

# 각 줄의 가장높이 있는 상자의 낙차가 각줄에서 가장 크다. **
# 상자의 낙차는 어떻게 구할 것인가????
# 낙차를 구하는 방법 : 현재 오른쪽에 비어있거나 높이가 자신보다 작은상자이면,
count = 0
max_box = boxes[0]
for b in range(len(boxes)):
    if max_box == boxes[b]:
        pass
    elif max_box < boxes[b]:
        count = 0
        max_box = boxes[b]
    else:
        count += 1

print(count)


#하나의 열의 낙차부터 구하기
# 1. 가장 왼쪽에 있는 열의 낙차구하기
max_cnt = 0 #
for j in range(0,len(boxes)):
    target = boxes[j]
    cnt = 0
    for i in range(j+1, len(boxes)): # 1번열부터 끝까지 순회
    # targat보다 작은 값을 가지는 열의 수를 계산
        if boxes[i] < target:
            cnt += 1
    if cnt > max_cnt:
        max_cnt = cnt

print(max_cnt)


# 2. 모든열의 낙차를 구하고, 최고 낙차 구하기