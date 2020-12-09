import sys
sys.stdin = open('BOJ 1764 듣보잡.txt')

N,M = map(int, input().split())
people = set()
people2 = set()
for i in range(N):
    people.add(input())
for i in range(M):
    people2.add(input())
#이 문제에서 젤 중요한것! 세트를 사용하면 교집합을 사용할 수 있다...>!
people_list = sorted(list(people&people2))

print(len(people_list))
for i in people_list:
    print(i)