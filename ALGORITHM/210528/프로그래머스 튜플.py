import sys
sys.stdin = open('프로그래머스 튜플.txt')

s = input()
s = s[2:-2]
s = s.split("},{")
s = sorted(s,key=len)
base_list = []

for i in s:
    i = i.split(',')
    for j in i:
        j = int(j)
        if j not in base_list:
                base_list.append(j)

print(base_list)

