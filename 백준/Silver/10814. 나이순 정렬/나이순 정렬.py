n = int(input())
users = []
for i in range(n):
    user = input().split()
    users.append(user)

s_users = sorted(users,key=lambda x: int(x[0]))

for j in s_users:
    print(*j)