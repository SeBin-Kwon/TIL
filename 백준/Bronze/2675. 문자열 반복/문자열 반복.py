t = int(input())
for _ in range(t):
    r, s = input().split()
    result = ''
    for i in range(len(s)):
        result += s[i]*int(r)
    print(result)