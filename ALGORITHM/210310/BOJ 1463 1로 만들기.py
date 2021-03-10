import sys
sys.stdin = open('BOJ 1463 1로 만들기.txt')

n = int(input())
# cnt = 0
# while n != 1:
#     if n % 3 == 0:
#         n //= 3
#     elif n % 2 == 0:
#         n //= 2
#     else:
#         n -= 1
#     cnt += 1
#     print(n)
#
# print(cnt)


dp = [0,0,1,1]

# dp[n] = min(dp[n-1] , dp[n//2], dp[n//3) + 1
for i in range(4, n+1):
    dp.append(dp[i-1]+1)
    if i%2 == 0:
        dp[i] = min(dp[i//2]+1, dp[i])
    if i%3 == 0:
        dp[i] = min(dp[i//3]+1, dp[i])

print(dp[n])