import sys
sys.stdin = open('1920.txt','r')

n = int(input())
a = list(map(int,input().split()))
m = int(input())
b = list(map(int,input().split()))

print(n,a,m,b)