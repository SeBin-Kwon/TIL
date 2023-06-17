phone_book = ["123","456","789"]


def solution(phone_book):
    answer = True
    for i in range(len(phone_book)-1):
        for j in range(1,len(phone_book)):
            if phone_book[i].find(phone_book[j]):
                answer = False
                break
    return answer

print(solution(phone_book))