# 🚨 에러 / 예외 처리 (Error/Exception Handling)

### 오류가 발생했을 때 중점적으로 봐야할 곳

> 제어가 되는 시점 => 조건 / 반복, 함수

1. `branches`

   모든 조건이 원하는대로 동작하는지

2. `for loops`

   반복문에 진입하는지, 원하는 횟수만큼 실행되는지

3. `while loops`

   for loops와 동일, 종료조건이 제대로 동작하는지

4. `function`

   함수 호출시, 함수 파라미터, 함수 결과

## 디버깅 (debugging)

- `print` 함수 활용
  - 특정 함수 결과, 반복/조건 결과 등 나눠서 생각, 코드를 bisection으로 나눠서 생각
- 개발 환경 (text editor, IDE) 등에서 제공하는 기능 활용
  - breakpoint, 변수 조회 등
- Python tutor 활용 (단순 파이썬 코드인 경우)
- 뇌컴파일, 눈디버깅

> 코드를 작성하다가..

- 에러 메시지가 발생하는 경우
  - 해당 하는 위치를 찾아 메시지를 해결
- 로직 에러가 발생하는 경우
  - 명시적인 에러 메시지 없이 예상과 다른 결과가 나온 경우
    - 정상적으로 동작하였던 코드 이후 작성된 코드를 생각해봄
    - 전체코드를살펴봄
    - 휴식을가져봄
    - 누군가에게 설명해봄
    - ...

## 에러와 예외

### 문법 에러 (Syntax Error)

- `SyntaxError`가 발생하면, 파이썬 프로그램은 실행이 되지 않음

- 파일이름, 줄번호, `^` 문자를 통해 파이썬이 코드를 읽어 나갈 때(parser) 문제가 발생한 위치를 표현

- 줄에서 에러가 감지된 가장 앞의 위치를 가리키는 캐럿(caret)기호(^)를 표시

  ```python
  File "<ipython-input-1-f8a097d0a685>", line 1 
  if else ^
  SyntaxError: invalid syntax
  ```

- `EOL (End of Line)`

  따옴표를 안적었을 경우

  ```python
  print('hello
  # File "<ipython-input-6-2a5f5c6b1414>", line 1 # print('hello
  #							^
  # SyntaxError: EOL while scanning string literal
  ```

- `EOF (End of File)`

  ()괄호를 안닫았을 경우

  ```python
  print(
  # File "<ipython-input-4-424fbb3a34c5>", line 1 # print(
  #			^
  # SyntaxError: unexpected EOF while parsing
  ```

- `Invalid syntax`

  :콜론을 안적었을 경우

  ```python
  while
  # File "<ipython-input-7-ae84bbebe3ce>", line 1 # while
  #				^
  # SyntaxError: invalid syntax
  ```

- `assign to literal`

  상수(literal: 변하지않는 값)에 값을 할당하려고 했을 경우

  - `'a' = 3` ,`True = 3` => SyntaxError

  ```python
  5=3
  # File "<ipython-input-28-9a762f2c796b>", line 1
  # 5=3
  # ^
  # SyntaxError: cannot assign to literal
  ```

  

## 예외 (Exception)

- 실행 도중 예상치 못한 상황을 맞이하면, 프로그램 실행을 멈춤
  - 문장이나 표현식이 문법적으로 올바르더라도 발생하는 에러
- 실행 중에 감지되는 에러들을 `예외(Exception)`라고 부름
- 예외는 여러 타입(type)으로 나타나고, 타입이 메시지의 일부로 출력됨
  - `NameError`, `TypeError` 등은 발생한 예외 타입의 종류(이름)
- 모든 내장 예외는 `Exception Class`를 상속받아 이뤄짐
- 사용자 정의 예외를 만들어 관리할 수 있음

- `ZereDivisionError`

  0으로 나누고자 할 때 발생

  ```python
  10/0
  # ---------------
  # ZeroDivisionError Traceback (most recent call last) # ----> 1 10/0
  # ZeroDivisionError: division by zero
  ```

- `NameError`

  namespace 상에 이름이 없는 경우

  ```python
   print(name_error)
  # ---------------------------
  # NameError Traceback (most recent call last) # ----> 1 print(name_error)
  # NameError: name 'name_error' is not defined
  ```

- `TypeError`

  타입 불일치

  ```python
  1 + '1'
  # --------------
  # TypeError Traceback (most recent call last)
  # ----> 1 1 + '1'
  # TypeError: unsupported operand type(s) for +: 'int' and 'str'
  
   round('3.5')
  # ---------------
  # TypeError Traceback (most recent call last)
  # ----> 1 round('3.5')
  # TypeError: type str doesn't define __round__ method
  ```

- `TypeError`

  arguments 부족

  ```python
  divmod()
  # ------------
  # TypeError Traceback (most recent call last) # ----> 1 divmod()
  # TypeError: divmod expected 2 arguments, got 0
  
  import random
  random.sample()
  # ---------
  # TypeError Traceback (most recent call last) # 1 import random
  # ----> 2 random.sample()
  # TypeError: sample() missing 2 required positional arguments: 'population' and 'k'
  ```

- `TypeError`

  arguments 개수 초과

  ```python
  divmod(1, 2, 3)
  # ---------
  # TypeError Traceback (most recent call last) # ----> 1 divmod(1, 2, 3)
  # TypeError: divmod expected 2 arguments, got 3
  
  import random
  random.sample(range(3), 1, 2)
  # --------
  # TypeError Traceback (most recent call last) # 1 import random
  # ----> 2 random.sample(range(3), 1, 2)
  # TypeError: sample() takes 3 positional arguments but 4 were given
  ```

- `TypeError`

  첫번째 인자 타입 불일치

  ```python
   import random random.sample(1, 2)
  # ------
  # TypeError Traceback (most recent call last)
  #       1 import random
  # ----> 2 random.sample(1, 2)
  # ~/.pyenv/versions/3.8.6/lib/python3.8/random.py in sample(self, population, k)
      population = tuple(population)
  if not isinstance(population, _Sequence):
  raise TypeError("Population must be a sequence or
  # TypeError: Population must be a sequence or set. For dicts, use list(d).
  ```

- `ValueError`

  타입은 올바르나 값이 적절하지 않거나 없는 경우

  ```python
  int('3.5')
  # ------
  # ValueError Traceback (most recent call last)
  # ----> 1 int('3.5')
  # ValueError: invalid literal for int() with base 10: '3.5'
  
  range(3).index(6)
  # ------
  # ValueError Traceback (most recent call last) # ----> 1 range(3).index(6)
  # ValueError: 6 is not in range
  ```

- `IndexError`

  ```python
  empty_list = []
  empty_list[2]
  # ------
  # IndexError Traceback (most recent call last) # 1 empty_list = []
  # ----> 2 empty_list[2]
  # IndexError: list index out of range
  ```

- `KeyError`

  ```python
  song = {'IU': '좋은날'}
  song['BTS']
  # ------
  # KeyError Traceback (most recent call last) # 1 song = {'IU': '좋은날'}
  # ----> 2 song['BTS'] # KeyError: 'BTS'
  ```

- `ModulNotFoundErre`

  존재하지 않는 모듈을 import 하는 경우

  ```python
  import nonamed
  # ------
  # ModuleNotFoundError Traceback (most recent call last) # ----> 1 import nonamed
  # ModuleNotFoundError: No module named 'nonamed'
  ```

- `ImportError`

  Module은 있으나 존재하지않는 클래스/함수를 가져오는 경우

  ```python
  from random import samp
  # ------
  # ImportError Traceback (most recent call last)
  # ----> 1 from random import samp
  # ImportError: cannot import name 'samp' from 'random'
  ```

- `IndentationError`

  Indentation(들여쓰기)이 적절하지 않는 경우

  ```python
  for i in range(3):
  print(i)
  # File "<ipython-input-56-78291925d94f>", line 2 # print(i)
  # ^
  # IndentationError: expected an indented block
  ```

- `KeyboardInter`

  임의로 프로그램을 종료하였을 때

  ```python
  while True: continue
  # ------
  # KeyboardInterrupt Traceback (most recent call last) # <ipython-input-55-6a65cf439648> in <module>
  # 1 while True:
  # ----> 2 continue
  # KeyboardInterrupt:
  ```

#### 파이썬 내장 예외의 클래스 계층 구조  (built-in-exceptions)

https://docs.python.org/ko/3/library/exceptions.html#exception-hierarchy

## 예외 처리

> try문 (statement) / except 절(clause)을 이용하여 예외 처리를 할 수 있음

- 에러가 발생했을 때 다른 행동을 할 수 있도록 함
- **try문은 반드시 한 개 이상의 except문이 필요**
- `try` 문
  - 오류가 발생할 가능성이 있는 코드를 실행
  - 예외가 발생되지 않으면, except 없이 실행 종료
- `except` 문
  - 예외가 발생하면, except 절이 실행
  - 예외 상황을 처리하는 코드를 받아서 적절한 조치를 취함
- `else`
  - `try` 문에서 예외가 발생하지 않으면 실행함
- `finally`
  - 예외 발생 여부와 관계없이 항상 실행함

### 예외처리 예시

```python
# 숫자 입력을 받아서 출력
numbers = input('숫자를 입력해주세요: ')
print(numbers)
try:
    if int(numbers) == 5:
        print('오오~')
    else:
        print('오가 아닙니다.')
except:
    print('숫자를 입력하지 않았습니다.')
    
# 100을 사용자가 입력한 숫자로 나눠서 결과를 출력
number = input()
try:
    print(100/int(number))
except ZeroDivisionError as err : 
# except (ValueError, ZeroDivisionError:) 한꺼번에 묶어서 예외처리 가능
    print(err)
    print('0으로 나눌 수는 없습니다.')
except ValueError:
    print('숫자 형식을 입력해주세요.')
except Exception:
    print('오류') # 상위의 개념이므로 하단부에 작성해야 한다.
```

- 파일을 열고 읽는 코드를 작성하는 경우

  - 파일 열기 시도
    - 파일 없는 경우 ⇒ ‘해당 파일이 없습니다.’ 출력 `(except)`
    - 파일 있는 경우 ⇒ 파일 내용을 출력 `(else)`
  - 해당 파일 읽기 작업 종료 메시지 출력 `(finally)`

  ```python
  파일이 없는 경우 
  try:
      f = open('nooofile.txt')
  except FileNotFoundError:
      print('해당 파일이 없습니다.') # 실행
  else:
      print('파일을 읽기 시작합니다.') 
      print(f.read())
      print('파일을 모두 읽었습니다.') 
      f.close()
  finally:
      print('파일 읽기를 종료합니다.') # 모두 실행
      
   
  
  파일이 있는 경우 
  try:
      f = open('file.txt') 
  except FileNotFoundError:
      print('해당 파일이 없습니다.') 
  else:
      print('파일을 읽기 시작합니다.') # 실행
      print(f.read())
      print('파일을 모두 읽었습니다.') 
      f.close()
  finally:
      print('파일 읽기를 종료합니다.') # 모두 실행
  ```



## 예외 발생 시키기

### raise statement

> `raise`를 통해 예외를 강제로 발생

- 에러라는 걸 알려주기 위함
- `raise <표현식> (메시지)`
  - <표현식> : 예외 타입 지정 
    - 주어지지 않을 경우 현재 스코프에서 활성화된 마지막 예외를 다시 일으킴

```python
raise
# -------
# RuntimeError Traceback (most recent call last) # ----> 1 raise
# RuntimeError: No active exception to reraise
```