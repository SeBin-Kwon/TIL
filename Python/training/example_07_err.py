# 아래 코드는 평균을 구하는 논리적으로 오류가 있는 코드입니다. 
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

total = 0
count = 0

for number in number_list:
    total += number
    count += 1

print(total / count)

# 리스트안에 요소가 반복될 때마다 count 값이 1씩 늘어나야하기 때문에 count를 반복문 안에 들여쓰기로 넣어주고 total과 count를 //로 몫을 구하는 것이 아닌 /로 나눠서 평균값을 구해야 한다.