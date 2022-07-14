# 실습 문제 풀이 3

## 문제 15

파이썬 튜터 확인해보기

a가 처음으로

'banana'

0 b False

1 a True

문자로 순회하는 것이 아니라 인덱스로 접근

=> range

for - else

boolean을 활용해서 for-else 대체 가능

얘가 들어왔는지 안들어왔는지 알고싶어

=> boolean



## 문제 16

if char == 'a' or char == 'e' or char == 'i'.. 이렇게 했어야함

if char in 'aeiou':

in이 결국엔 반복문



## 문제 18

banana

#### 왜 딕셔너리인가?

b 1

a 1 어? a 있네? 2

n 1

있으면? +1 없으면? 0



##### 딕셔너리에 키가 없으면?

if not char in result:

캐릭터가 딕셔너리안에 없으면

키랑 값을 1로 초기화한다.

result[char] = 1

##### 딕셔너리에 키가 있으면?

else:

result[char] += 1

기존것에 더해준다

2.

result['a'] 없