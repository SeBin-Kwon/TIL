s,k,h = list(map(int,input().split()))
if s+k+h >= 100:
    print('OK')
elif s+k+h < 100:
    if s < k and s < h:
        print('Soongsil')
    elif k < s and k < h:
        print('Korea')
    elif h < s and h < k:
        print('Hanyang')