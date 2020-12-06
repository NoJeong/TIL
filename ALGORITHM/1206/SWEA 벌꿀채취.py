import sys
sys.stdin = open('SWEA 벌꿀채취.txt')

def calc(idx,sum_honey,sum_cost):
    global max_cost
    if sum_honey > C:
        return
    max_cost = max(max_cost, sum_cost)

    for i in range(idx, M):
        calc(i+1,sum_honey + honey[i], sum_cost + honey[i] ** 2)

for tc in range(1,int(input())+1):
    N,M,C = map(int, input().split()) #한변의 길이, 채취할 벌통의 길이, 한일꾼의 최대벌꿀

    arr = [list(map(int, input().split())) for _ in range(N)]
    honey_list = []

    #순회하면서 벌통을 뽑아보기
    for i in range(N):
        for j in range(N-M+1): #가로로 연속된 통을 뽑기때문에 모두 실행해볼 필요는 없음
            honey = arr[i][j:j+M]
            max_cost = 0
            calc(0,0,0)
            honey_list.append((max_cost, i, j))

    honey_list.sort(reverse=True)
    first = honey_list.pop(0)
    for cost,r,c, in honey_list:
        if r == first[1] and first[2] - M < c < first[2] + M:
            continue
        second = [cost,r,c]
        break
    print('#{} {}'.format(tc, first[0] + second[0]))
