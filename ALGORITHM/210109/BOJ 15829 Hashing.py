import sys
sys.stdin = open('BOJ 15829 Hashing.txt')

L = int(input())
base = input()
count = 0
summ = 0
for i in base:
    summ += (ord(i)-96) * 31**count
    count += 1
if summ >= 1234567891:
    print(summ % 1234567891)
else:
    print(summ)