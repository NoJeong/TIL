import sys
sys.stdin = open('SWEA 보물상자 비밀번호.txt')

def hex_to_dec(num16):
    value = 0

    for i in range(len(num16)):
        if '0' <= num16[i] <= '9':
            tmp = ord(num16[i]) - ord('0')
        else:
            tmp = ord(num16[i]) - ord('A') + 10
        value += tmp * (16 ** (L-1-i))

    return value


for tc in range(1,int(input())+1):
    N, K = map(int, input().split())
    password = list(input())
    ans = set()
    ans1 = set()
    L = N//4

    for i in range(L):
        for j in range(0, N, L):
            ans.add(''.join(password[j:j+L]))
            ans1.add(int(''.join(password[j:j+L]),16))

        password.insert(0,password.pop())

    ans = list(ans)
    ans1 = list(ans1)
    ans.sort(reverse=True)
    ans1.sort(reverse=True)
    print(ans1[K-1])
    print("#{} {}".format(tc, hex_to_dec(ans[K-1])))


    #############################################################

for tc in range(1,int(input())+1):
    N, K = map(int, input().split())
    password = list(input())
    ans = set()
    password += password[:L-1]

    for i in range(N):
        ans.add(int(''.join(password[i:i+L]),16))
    ans = list(ans)
    ans.sort(reverse=True)
    print(ans[K-1])