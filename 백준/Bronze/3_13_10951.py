while True:
    try:
        a,b = map(int, input().split())
        print(a+b)
    except:
        break
    
# import sys
# for line in sys.stdin:
#     print(sum(map(int,line.split())))