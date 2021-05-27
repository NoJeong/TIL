import sys
sys.stdin = open('1.txt')

n = int(input())

dump_list = []
answer = 0
a = n
while a > 0:
    dump_list.append(a % 10)
    a = a // 10
b = sorted(dump_list,reverse=True)

increase = 1
while b:
    answer += b.pop(-1) * increase
    increase *= 10

print(answer)