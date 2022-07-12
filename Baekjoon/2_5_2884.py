h, m = map(int,input().split())
if m < 45:
    m = m-45+60
    if h == 0:
        h += 23
    else:
        h = h-1
else:
    m -= 45
print(h, m)

# a,b=map(int,input().split())
# c=a*60+b-45
# print(c//60%24, c%60)

# h,m=map(int,input().split())
# m-=45
# if m<0:
#     m+=60
#     h-=1
#     if h<0:
#         h=23
# print(h,m,sep=' ')