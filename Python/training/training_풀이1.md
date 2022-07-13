# 실습 문제 풀이 1

## 문제 6 최대값 구하기

[0, 20, 100, 40]

1. 0과 20 비교 -> 최대값 20 기록

2. 20과 100 비교 -> 최대값 100 기록

3. 100과 40 비교 -> 최대값 기록 안함

4. for문으로 반복하기

5. 만약 최대값이 n보다 작으면 바꾼다 (참)

- 주의! 초기값 0인 경우 음수의 최대값을 구할 수 없다.
  - 리스트로 접근 혹은 초기값을 가장 작은 것을 할당(`float("-inf")`)

```python
# 최댓값 구하기
numbers = [-10, -100, -30]
# max_num = float("-inf")
max_num = numbers[0]
# 1. 반복
for n in numbers:
    # print(n)
    # 2. 만약, max값이 n보다 작으면 바꾼다.
    if max_num < n:
        # print('왔냐?')
        max_num = n 
print(max_num)
```



## 문제 8 두번째로 큰 수 구하기

1. 변수 최대값, 변수 두번째 큰 수로 총 2개 변수 세우기

2. 최대보다는 n이 작지만 두번째 최대값보다는 큰 경우
3. 왜 40이라는 수가 두번째로 크다고 생각하는지 고찰하기

```python
numbers = [0, 20, 100, 40]
#float("-inf") 문제 조건중 가장 작은 수로 하면 됨.
max_number = numbers[0]
second_number = numbers[0]
#1. 전체 숫자를 반복
for n in numbers:
  # 만약에, n이 최대보다 크다면
  if max_number < n:
     # 최대값이었던 것이 두번째로 큰 수
     second_number = max_number
     max_number = n
 # elif secone_number < n < max_number:
    elif secone_number < n and n < max_number:
    second_number = n
print(second_number)
```
