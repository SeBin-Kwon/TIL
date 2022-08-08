l = []
dict = {}
for _ in range(10):
    n = int(input())
    l.append(n)
    if n not in dict:
        dict[n] = 1
    else:
        dict[n] += 1
print(sum(l)//10,max(dict,key=dict.get), sep='\n')
    