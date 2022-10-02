import sys
sys.stdin = open('2002.txt','r')

# 순서 기록할 딕셔너리
dic = {}
# 추월한 개수
cnt = 0

n = int(input())

# 들어온 차량, 나간 차량 리스트에 저장
in_ = [input() for _ in range(n)]
out_ = [input() for _ in range(n)]

# 딕셔너리에 들어온 순서 저장
for k in range(n):
    dic[in_[k]] = k
# {'ZG431SN': 0, 'ZG5080K': 1, 'ST123D': 2, 'ZG206A': 3}

# 나간 차량 리스트에서 차례대로 비교
for i in range(n-1):
    for j in range(i+1,n):
        # 만약 먼저 나간 차량이 뒤에 차보다
        # 들어온 순서가 크다면 추월한 것
        if dic[out_[i]] > dic[out_[j]]:
            cnt += 1
            # 중복으로 카운트되지 않게 break해준다.
            break
print(cnt)