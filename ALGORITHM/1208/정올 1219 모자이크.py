import sys
sys.stdin = open('정올 1219 모자이크.txt')

def paper(ans1,cnt):
    global ans
    for i in range(1,M+1):
        for j in range(1,N+1):
            if base[j][i] == 1:
                cnt += 1
                print(cnt,'cnt')
                for a in range(i,i+ans1):
                    for b in range(j,j+ans1):
                        # print('b',(j,j+ans))
                        if 0 < a <= M and 0 < b <= N and base[b][a] == 1:
                            base[b][a] = 0
                print(*base,sep='\n')

    if cnt < papers:
        paper(ans1-1,0)
        ans-=1
    elif cnt == papers:
        return ans



N,M = map(int,input().split())
papers = int(input())
wrong = int(input())
base = list([0]*(M+1) for _ in range(N+1))
for i in range(wrong):
    a, b = map(int, input().split())
    base[a][b] = 1
print(*base,sep='\n')
ans = N
cnt = 0

result = paper(ans,cnt)
print(result)
print(ans)