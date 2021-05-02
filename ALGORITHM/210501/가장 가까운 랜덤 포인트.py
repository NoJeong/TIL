import sys
sys.stdin = open('가장 가까운 랜덤 포인트.txt')

nx = int(input())
x = []
for i in range(nx):
    x.append(int(input()))

ny = int(input())
y = []
for i in range(ny):
    y.append(int(input()))

min_value = ((x[0]-x[1])**2 + (y[0]-y[1])**2)

for i in range(len(x)-1):
        for j in range(1,len(x)):
            temp_value = ((x[i]-x[j])**2 + (y[i]-y[j])**2)
            if temp_value < min_value:
                min_value = temp_value
print(min_value)