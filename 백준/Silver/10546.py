import sys
sys.stdin = open('10546.txt', 'r')
input = sys.stdin.readline

n = int(input())
runner = {}
for i in range(n+(n-1)):
    name = input()
    if name not in runner:
        runner[name] = 1
    else:
        runner[name] += 1

for k,v in runner.items():
    if v % 2 != 0:
        print(k)
        break

    # runner[name] = runner.get(runner[name], 0) + 1