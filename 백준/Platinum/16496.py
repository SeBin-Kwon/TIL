import sys
from functools import cmp_to_key
sys.stdin = open('16496.txt', 'r')
input = sys.stdin.readline

def compare(a, b):
    str1 = a + b
    str2 = b + a
    return (int(str1) > int(str2)) - (int(str1) < int(str2))

n = int(input())
numbers = input().split()
numbers.sort(key= cmp_to_key(compare), reverse= True)
print(str(int("".join(numbers))))