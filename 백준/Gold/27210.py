import sys
sys.stdin = open('27210.txt','r')
input = sys.stdin.readline

n = int(input())
stones = list(map(int, input().split()))

if n == 1:
    print(1)
else:
    left, right, max_left, max_right = 0, 0, 0, 0
    for stone in stones:
        if stone == 1:
            left += 1
            if right != 0:
                right -= 1
            else:
                right = 0
        else:
            right += 1
            if left != 0: 
                left -= 1
            else:
                left = 0
        max_left = max(max_left, left)
        max_right = max(max_right, right)
    print(max(max_left,max_right))


