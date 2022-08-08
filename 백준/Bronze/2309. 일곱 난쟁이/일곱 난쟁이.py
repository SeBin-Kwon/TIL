dwarfs = []
for _ in range(9):
    dwarf = int(input())
    dwarfs.append(dwarf)
total = sum(dwarfs)

for i in range(8):
    for j in range(i+1,9):
        if total - (dwarfs[i] + dwarfs[j]) == 100:
            f1 = dwarfs[i]
            f2 = dwarfs[j]
dwarfs.remove(f1)
dwarfs.remove(f2)
print(*sorted(dwarfs),sep='\n')