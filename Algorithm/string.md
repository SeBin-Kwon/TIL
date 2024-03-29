# 🔖 문자열 (String)

> 문자열은 **immutable(변경 불가능한)** 자료형
>
> **iterable(순회가능한)** 자료형

<br>

## 1. 문자열 슬라이싱

- 슬라이싱은 새로운 문자열 생성
  - 새로운 주소값을 가지게 됨
  - 원래 문자열은 변수 바인딩에서 풀리게 됨

### 예시

```python
s = 'abcdefghi'
```

- `s[2:5]`

  'cde'

- `s[-6:-2]`

  'defg'

  - `s[9-6:9-2]` 음수는 원래 길이에서 빼면 양의 인덱스를 알수있음

- `s[2:-4]`

  'cde'

- `s[2:5:2]`

  'ce'

- `s[-6:-1:3]`

  'dg'

- `s[2:5:-1]`

  ''

- `s[5:2:-1]`

  'fed'

- `s[:3]`

  'abc'

- `s[5:]`

  'fghi'

- `s[:]`

  'abcdefghi'

- `s[::-1]`

  'ihgfedcba'

- `s[10:20]`

  ''

#### 문자열 슬라이싱 연습

#### https://www.acmicpc.net/problem/10988

<br>

## 2. 문자열 메서드

- `.split(기준 문자)` => `O(N)`
  - 문자열을 일정 **기준**으로 나누어 **리스트로 반환**
  - 괄호 안에 아무것도 넣지 않으면 자동으로 공백을 기준으로 설정
- `.strip(제거할 문자)` => `O(N)`
  - 문자열의 **양쪽** 끝에 있는 특정 문자를 모두 **제거**한 새로운 문자열 반환
  - 괄호 안에 아무것도 넣지 않으면 자동으로 공백을 제거 문자로 설정
  - 제거할 문자를 여러 개 넣으면 해당하는 모든 문자들을 제거
- `.find(찾는 문자)` => `O(N)`
  - 특정 문자가 처음으로 나타나는 **위치(인덱스)**를 반환
  - 찾는 문자가 없다면 **-1**을 반환
- `.index(찾는 문자)` => `O(N)`
  - 특정 문자가 처음으로 나타나는 **위치(인덱스)**를 반환
  - 찾는 문자가 없다면 **오류**발생
    - 실행을 멈춤
- `.count(개수를 셀 문자)` => `O(N)`
  - 문자열에서 특정 문자가 **몇 개**인지 반환
  - 문자 뿐만 아니라, 문자열의 개수도 확인 가능

- `.replace(기존 문자, 새로운 문자)` => `O(N)`
  - 문자열에서 기존 문자를 새로운 문자로 **수정**한 새로운 문자열 반환
  - 특정 문자를 빈 문자열('')로 수정하여 마치 해당 문자를 삭제한 것 같은 효과 가능
- `삽입할 문자.join(iterable)` => `O(N)`
  - iterable의 **각각 원소 사이에 특정 문자를 삽입**한 새로운 문자열 반환
  - 공백 출력, 콤마 출력 등 원하는 **출력** 형태를 위해 사용

### 문자열 메서드 연습

https://www.acmicpc.net/problem/17249

<br>

## 3. 아스키(ASCII) 코드

>컴퓨터는 숫자만 이해할 수 있다

- `비트(bit)`
  - 0과 1 두 가지 정보만 표현
- `바이트(byte)`
  - 데이터를 저장하는 기본 단위
  - `1 byte == 8 bits`

### ASCII (미국 정보교환 표준부호)

> 알파벳을 표현하는 대표 인코딩 방식

- 각 문자를 표현하는데 1 byte(8 bits) 사용
  - 1bit : 통신 에러 검출용
  - 7bit : 문자 정보 저장 (총 128개)
- `ord(문자)`
  - **문자 => 아스키코드**로 변환하는 내장함수
- `chr(아스키코드)`
  - **아스키코드 => 문자**로 변환하는 내장함수

### 아스키(ASCII) 코드 연습

https://www.acmicpc.net/problem/10809