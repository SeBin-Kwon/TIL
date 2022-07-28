a, b = map(int,input().split()) 
result = []    
for i in range(b+1):     
    num = [i]*i 
    result += num    
print(sum(result[a-1:b])) 