import sys
sys.stdin = open('2.txt')

base = list(map(int,input().split()))
print(base)

dump_list = set()
for i in range(len(base)-1):
    for j in range(i+1,len(base)):
        dump_list.add(base[i] + base[j])
a = list(dump_list)
b = sorted(a)

print(b)