tae = input()

print(tae[0:tae.find('0')].count('@'), tae[tae.find('0'):len(tae)].count('@'))

# print(*[a.count('@')for a in input().split('0')])

# a,b=input().split("(^0^)")
# print(a.count('@'),b.count("@"))