import sys
sys.stdin = open('2775.txt', 'r')

# a층의 b호에 살려면 자신의 아래(a-1)층의 1호부터 b호까지 사람들의 수의 합만큼 사람들을 데려와 살아야 한다”

#  양의 정수 k와 n에 대해 k층에 n호에는 몇 명이 살고 있는지 출력하라. 단, 아파트에는 0층부터 있고 각층에는 1호부터 있으며, 0층의 i호에는 i명이 산다.

T = int(input())
for t in range(T):
    k = int(input())
    n = int(input())
    s = [i for i in range(1,n+1)]
    for j in range(k):
        for k in range(1,n):
            s[k] += s[k-1]
    print(s[-1])
