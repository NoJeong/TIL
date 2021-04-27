import sys
sys.stdin = open('BOJ 7568 덩치.txt')

tc = int(input())
base_list = []
for i in range(tc):
    temp = []
    temp.append(list(map(int, input().split())))
    temp.append(1)
    # print(temp)
    base_list.append(temp)

for i in range(len(base_list)):
    for j in range(len(base_list)):
        if base_list[i][0][0] < base_list[j][0][0] and base_list[i][0][1] < base_list[j][0][1]:
            base_list[i][1] += 1

for i in range(len(base_list)):
    print(base_list[i][1], end=' ')