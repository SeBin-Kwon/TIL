import sys
sys.stdin = open('2979.txt', 'r')

m = list(map(int,input().split()))
time = []
total = 0
k = 0

for _ in range(3):
    time.append(list(map(int,input().split())))

s_time = sorted(time, key=lambda x : (x[0], x[1]))

for i in range(3):
    p = s_time[i][1] - s_time[i][0]
    total += p * m[2-i]
print(total)