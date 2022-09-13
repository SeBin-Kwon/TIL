import sys
sys.stdin = open('10814.txt','r')

#todo 나이와 이름 가입한 순서대로 주어짐
#todo 회원들 나이가 증가하는 순(나이 오름차순),
#todo 나이가 같으면 먼저 가입한 사람이 앞에 오는 순서로 정렬

n = int(input())
users = []
for i in range(n):
    user = input().split()
    users.append(user)

s_users = sorted(users,key=lambda x: int(x[0]))

for j in s_users:
    print(*j)