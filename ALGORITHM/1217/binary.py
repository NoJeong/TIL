import sys
sys.stdin = open('binary.txt')

temp = input()
base = []
for i in range(len(temp)):
    base.append(int(temp[i]))
mid_result = []
mid_result_sum = []
result = []
for i in range(len(base)):
    mid_result.append(base[i])
    if len(mid_result)==7:
        for k in range(6,-1,-1):
            mid_result_sum.append(mid_result[k] * (2 ** abs(k-6)))
            mid_result.pop()
        result.append(sum(mid_result_sum))
        mid_result_sum = []
print(result)