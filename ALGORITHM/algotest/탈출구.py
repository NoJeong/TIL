import sys
sys.stdin = open('탈출구.txt')

for tc in range(1,int(input())+1):
    N = int(input())
    base = [list(map(int, input().split())) for _ in range(N)]
    # print(*base,sep='\n')
    person = []
    road = []
    for i in range(len(base)):
        for j in range(len(base[i])):
            if base[i][j] == 1:
                person.append((i,j))
            elif base[i][j] == 2:
                road.append((i,j))
    # print(person)
    # print(road)

    road_1 = []
    road_2 = []
    for i in range(len(person)):
        road_1.append([abs(road[0][0] - person[i][0]) + abs(road[0][1] - person[i][1]) + 1, 1])
        road_2.append([abs(road[1][0] - person[i][0]) + abs(road[1][1] - person[i][1]) + 1, 2])
    # print(road_1)
    # print(road_2)
    comb_array = []

    max_num = []
    def calc(array):
        a = sorted(array, key= lambda x : (x[1], x[0]))
        # print(a)
        num = []
        for i in range(len(a)):
            for j in range(i+1,len(a)):
                if a[i][1] == a[j][1] and a[i][0] == a[j][0]:
                    a[j][0] += 1
            # print('1',a)
            num.append(a[i][0])
        # print(num)
        max_num.append(max(num))
        # print(max_num)
        # print(min(max_num))
    def comb(n):
        if len(comb_array) == len(person):
            # print(comb_array)

            calc(comb_array)
            return

        comb_array.append(road_1[n])
        # comb_visit[i] = True
        comb(n+1)
        comb_array.pop()
        # comb_visit[i] = False
        comb_array.append(road_2[n])
        # comb_visit[i] = True
        comb(n + 1)
        comb_array.pop()
        # comb_visit[i] = False
    comb(0)
    print(f'#{tc} {min(max_num)}')