nums = input().split('-')
s = 0
for i in nums[0].split('+'):
    s += int(i)
for j in nums[1:]:
    for k in j.split('+'):
        s -= int(k)
print(s)