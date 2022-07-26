n = int(input())
for i in range(n):
    if i%2 == 0:
        print('* '*n)
    else:
        print(' *'*n)

# for i in range(n):
#     print(('* ' if i%2 == 0 else ' *')*n)