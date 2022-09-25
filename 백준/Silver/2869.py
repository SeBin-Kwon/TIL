import sys
sys.stdin = open('2869.txt','r')
import math
input = sys.stdin.readline

a, b, v = map(int,input().split())
day = (v-b) / (a-b)
print(math.ceil(day))