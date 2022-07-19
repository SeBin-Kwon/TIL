# 실습 문제 풀이 5

## 문제 20 각 자릿수의 합 구하기

```python
number = 123

#number가 0일 때 stop
# => int는 0일 때 False
result = 0
while number:
  # 몫은 다음 number가 됨
  # 나머지는 더해나가기
  # 1.
  result += number%10
  number //= 10
  
  # 2.
  # divmod(x,y)는 x를 y로 나누고,
  # 결과를 tuple로 변환
  # (몫, 나머지)
  result, remainder = divmod(number, 10)
  result += remainder
  
print(result)
```



## 문제 21 숫자 뒤집기

```python
number = 123
# print(int(str(number)[::-1]))
result = 0
while number:
  # 이전 결과에 10을 곱하고
  result *= 10
  # 나머지를 더해주고
  result += number%10
  # number를 깎는다.
  number //= 10
```

0 => 0+3 , 12 => 30+2, 1 => 320+1, 0 => False, break