import sys
sys.stdin =open('BOJ 2775 부녀회장이 될테야.txt')

# N =int(input())
# for tc in range(N):
#     floor = int(input())
#     room = int(input())
#     hotel =[]
#     temp = []
#     for j in range(1,room+1):
#         temp.append(j)
#     hotel.append(temp)
#     for i in range(floor+1):
#         hotel.append([0]*room)
#     for i in range(1,floor+1):
#         for j in range(room):
#             temp1 = 0
#             for k in range(j+1):
#                 temp1 += hotel[i-1][k]
#             hotel[i][j] = temp1
#     print(hotel[floor][room-1])



    ##########################################
    #다른사람의 코드

T = int(input())

for _ in range(T):

    k = int(input())

    n = int(input())

    people = [i for i in range(1, n + 1)]

    for __ in range(k):

        for j in range(1, n):
            people[j] += people[j - 1]

    print(people[-1])