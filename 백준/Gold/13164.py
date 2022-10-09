import sys
sys.stdin = open('13164.txt', 'r')
input = sys.stdin.readline

n, k = map(int,input().split())
# 키 순서대로 줄 세웠다. 이미 오름차순 정렬
l = list(map(int,input().split()))
