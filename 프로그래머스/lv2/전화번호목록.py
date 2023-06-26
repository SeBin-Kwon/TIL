phone_book = ["12", "567", "123","1235","88"]

def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            answer = False
    return answer


# def solution1(phoneBook):
#     phoneBook = sorted(phoneBook)

#     for p1, p2 in zip(phoneBook, phoneBook[1:]):
#         if p2.startswith(p1):
#             return False
#     return True

# def solution2(phone_book):
#     answer = True
#     hash_map = {}
#     for phone_number in phone_book:
#         hash_map[phone_number] = 1
#     print(hash_map)
#     for phone_number in phone_book:
#         temp = ""
#         for number in phone_number:
#             temp += number
#             print('temp: ',temp)
#             if temp in hash_map and temp != phone_number:
#                 answer = False
#                 print(temp,phone_number)
#     return answer

# def solution(phone_book): 
#     for i in range(len(phone_book)): 
#         pivot = phone_book[i] 
#         for j in range(i+1, len(phone_book)): 
#             strlen = min(len(pivot), len(phone_book[j])) 
#             if pivot[:strlen] == phone_book[j][:strlen]: 
#                 return False 
#     return True

print(solution(phone_book))