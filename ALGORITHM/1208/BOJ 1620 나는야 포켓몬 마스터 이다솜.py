import sys
sys.stdin = open('BOJ 1620 나는야 포켓몬 마스터 이다솜.txt')

#
# M,N = map(int,input().split())
#
# poke_dic = {}
# poke_list = [0]
# for i in range(1,M+1):
#     a = input()
#     if not a in poke_dic:
#         poke_dic[a] = str(i)
#         poke_list.append(a)
# # print(poke_dic)
# for i in range(N):
#     a = input()
#     if a.isalpha():
#         print(poke_dic[a])
#
#     if a.isdigit():
#         print(poke_list[int(a)])

import sys
input = sys.stdin.readline

M,N = map(int,input().split())

poke_dic = {}
poke_list = [0]
idx = 1
for i in range(M):
    a = input().rstrip()
    if not a in poke_dic:
        poke_dic[a] = str(idx)
        poke_list.append(a)
    idx += 1
# print(poke_dic)
for i in range(N):
    a = input().rstrip()
    if a.isalpha():
        print(poke_dic[a])

    if a.isdigit():
        print(poke_list[int(a)])