# 현재 시각에 요리 시간을 더해서 종료 시간 구하기
h, m = map(int,input().split())
cook = int(input())
t = h * 60 + m + cook
print(t//60%24, t%60)
