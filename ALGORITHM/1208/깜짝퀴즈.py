def go(idx):
    global ans1
    if idx == len(base):
        back(idx-1)
        return
    # print(base[idx])
    ans1.append(base[idx])
    go(idx+1)
def back(idx):
    global ans2
    if idx< 0:
        return
    # print(base[idx])
    ans2.append(base[idx])
    back(idx-1)

base = 'ASADADAS'
ans1 =[]
ans2 =[]
go(0)
print(*ans1)
print(*ans2)