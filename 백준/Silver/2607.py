import sys
sys.stdin = open('2607.txt', 'r')
input = sys.stdin.readline

n = int(input())
first = list(input().rstrip())
answer = 0

for i in range(n-1):
    compare = first[:]
    word = input().rstrip()
    cnt = 0
    for w in word:
        if w in compare:
            compare.remove(w)
        else:
            cnt += 1
    if cnt < 2 and len(compare) < 2:
        answer += 1
print(answer)

# n = int(input())
# first = input().rstrip()
# f_dic = {}
# result = 0

# for i in first:
#     if i not in f_dic:
#         f_dic[i] = 1
#     else:
#         f_dic[i] += 1
        
# for i in range(n-1):
#     c_dic = f_dic.copy()
#     word = input().rstrip()
#     cnt = 0
#     flag = False
#     for j in word:
#         if j in c_dic:
#             c_dic[j] -= 1
#         else

    # for k, v in dic.items():
    #     if k in c_dic:
    #         if (c_dic[k] - v) < 0:
    #             cnt += 1
    #         c_dic[k] -= v
    #     else:
    #         cnt += v
    # if cnt <= 1 and abs(sum(c_dic.values())) <= 1:
    #     result += 1
# print(result)