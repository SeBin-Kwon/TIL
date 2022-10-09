

s = "3people unFollowed me"
l = s.split()
result = ''
for i in range(len(l)):
    if l[i][0].isdigit():
        result += l[i].lower() + ' '
    else:
        if i != len(l):
            result += l[i].title() + ' '
        else:
            result += l[i].title()
print(result.rstrip())

def solution(s):
    l = s.split()
    result = ''
    for i in l:
        if i[0].isdigit():
            result += i.lower() + ' '
        else:
            result += i.title() + ' '

    return result.rstrip()

# def solution(s):
#     answer = s.title()

# def solution(s):
#     return " ".join([i.title() for i in s.split(' ')])
# print(solution("3people unFollowed me"))