# 실습 문제 풀이 3

## 문제 12 문자열 조작하기

'apple' -> pple -> 변수 result

while? for? -> for : 왜냐하면 하나를 끝까지 반복하니깐

만약에 if 단어가 a 일 때 -> 기록하지 않는다.

```python
# 주어진 문자열 word가 주어질 때, 해당 단어에서 ‘a’를 모두 제거한 결과를 출력하시오.
word = 'apple'
result = ''
# 반복! for
for char in 'apple':
  # 만약 a 일 때
  if char == 'a':
  	# 반복문에서 아무것도 안하고 넘어가는 것은?
    # continue
    continue
  result = result + char
  # 만약 a가 아닐 때
  if char != 'a':
    result = result + char
print(result)
```



## 문제 13 문자열 조작하기

```python
# 주어진 문자열 word가 주어질 때, 해당 단어를 역순으로 뒤집은 결과를 출력하시오.
word = 'apple'

# 1. for
result = ''
for char in word:
    result = char + result
print(result)

# 2. pythonic
print(word[::-1])
print(''.join(reversed(word)))

# 3. index
# 익숙해질수록 나중에 알고리즘 코드 풀기 좋아요!
word = 'apple'

for i in range(len(word)):
    print(word[len(word)-i-1], end='')
```

### index 풀이

- `word`의 길이을 `len()`으로 구하고 `range`로 만든 후, `for문`에 넣는다.
  - 이때 `range`안의 값들은 `0 1 2 3 4`
  - 이것들을 변수 `i`에 반복적으로 넣음
- `word`의 `len()`값 `- i`를 하면 값이 `5 4 3 2 1` 이렇게 나옴
- 이것을 다시 `word[]`로 인덱싱을 하는 동시에 
  - 이때는 `word[5], word[4], word[3], word[2], word[1]`
- 원래 `word`의 인덱싱 값을 맞추기 위해 `-1`을 해줌

