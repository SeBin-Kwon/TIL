import sys
sys.stdin = open('18110.txt', 'r')
input = sys.stdin.readline

def my_round(x):
    if x - int(x) >= 0.5:
        return int(x) + 1
    else:
        return int(x)

n = int(input())
if n:
    comments = [int(input()) for _ in range(n)]
    comments.sort()
    remove_num = my_round(n * 0.15)
    print(my_round(sum(comments[remove_num:-remove_num] if remove_num else comments) / (n - 2 * remove_num)))
else:
    print(0)
