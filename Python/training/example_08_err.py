# 아래 코드는 문자열에서 모음의 개수를 찾는 코드입니다. 
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.
word = "HappyHacking"

count = 0

for char in word:
    if char == "a" or char ==  "e" or char ==  "i" or char ==  "o" or char ==  "u":
        count += 1

print(count)

# if문에서 or은 양쪽 식을 비교할때 모두 완성된 식을 비교해야한다.