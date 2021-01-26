base_list = []
def self_num(n):
    temp = n
    for i in str(n):
        temp += int(i)
    return temp

self_num(1)
for i in range(1, 10001):
    base_list.append(self_num(i))
for i in range(1, 10001):
    if i not in base_list:
        print(i)

# print(base_list)