tae = input()

print(tae[0:tae.find('0')].count('@'), tae[tae.find('0'):len(tae)].count('@'))