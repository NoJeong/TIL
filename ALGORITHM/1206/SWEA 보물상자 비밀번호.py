import sys
sys.stdin = open('SWEA 보물상자 비밀번호.txt')

for tc in range(1,int(input())+1):
    N,K = map(int,input().split())
    base = list(input())
    ans = set()
    L = N // 4
    for i in range(L):
        for j in range(0,N,L):
            ans.add(int(''.join(base[j:j+L]),16))
        base.append(base.pop(0))
    ans = list(ans)
    ans.sort(reverse=True)
    print(ans[K-1])