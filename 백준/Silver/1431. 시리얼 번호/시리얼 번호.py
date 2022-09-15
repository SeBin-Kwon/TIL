n = int(input())
s_num = []
for _ in range(n):
    s_num.append(input())

# 사전순 정렬
s_num.sort()

# 자리수 합 딕셔너리 생성
dic = {}
for i in range(n):
    sum_ = 0
    for j in range(len(s_num[i])):
        if 47 < ord(s_num[i][j]) < 58:
            sum_ += int(s_num[i][j])
    dic[s_num[i]] = sum_

s_dic = dict(sorted(dic.items(), key= lambda x: x[1]))

# 길이순 정렬
result = sorted(s_dic,key=len)

print(*result, sep='\n')