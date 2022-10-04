import sys
input = sys.stdin.readline
dp = [0]*1001 # 배열을 미리 다 만들고
dp[1]=1
dp[2]=2
dp[3]=3

for i in range(4,1001):
    # 해당 위치에 값을 할당
    dp[i] = (dp[i-1]+dp[i-2])%10007
n = int(input())
print(dp[n])

#? s = [0, 1, 2]
# 해당 위치에 값을 넣어놓고
#? for i in range(3, 1001):
# 순차적으로 값을 넣기
#?   s.append(s[i - 2] + s[i - 1])
#? n = int(input())
#? print(s[n] % 10007)