n = int(input())
for _ in range(n):
    a, b = input().split()
    
    A = sorted(a)
    B = sorted(b)

    if A == B:
        print(f'{a} & {b} are anagrams.')
    else:
        print(f'{a} & {b} are NOT anagrams.')