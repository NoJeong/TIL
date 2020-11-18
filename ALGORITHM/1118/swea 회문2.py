# arr = [[1,2,3],[2,3,4],[4,5,6]]
#
# test = list(zip(*arr))
#
# for row in test:
#     print(row)


def check_pal(M): #회문의 길이를 입력받아서 해당 길이의 회문이 있는지 없는지 판단
    for i in range(100):
        for j in range(100-M+1):
            #회문검사
            #회문검사 대상 추출
            tmp = board[i][j:j+M]
            tmp2 = zboard[i][j:j+M]
            if tmp == tmp[::-1] or tmp2 == tmp2[::-1]:
                return True
    return False
T = 10

for x in range(T):
    tc = int(input())
    board = [input() for _ in range(100)]
    zboard = list(zip(*board))#전치행렬
    #가로에 회문이 있는지 검사
    #전치 행렬의 가로 검사하면, 원래행렬의 세로 검사와 같다.
    #가장 긴 회문을 찾으면 되니까, 긴것부터 검사하면 된다.
    result = 0
    for i in range(100,0,-1):
        if check_pal(i):
            result = i
            break
