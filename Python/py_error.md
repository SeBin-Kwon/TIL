# π¨ μλ¬ / μμΈ μ²λ¦¬ (Error/Exception Handling)

### μ€λ₯κ° λ°μνμ λ μ€μ μ μΌλ‘ λ΄μΌν  κ³³

> μ μ΄κ° λλ μμ  => μ‘°κ±΄ / λ°λ³΅, ν¨μ

1. `branches`

   λͺ¨λ  μ‘°κ±΄μ΄ μνλλλ‘ λμνλμ§

2. `for loops`

   λ°λ³΅λ¬Έμ μ§μνλμ§, μνλ νμλ§νΌ μ€νλλμ§

3. `while loops`

   for loopsμ λμΌ, μ’λ£μ‘°κ±΄μ΄ μ λλ‘ λμνλμ§

4. `function`

   ν¨μ νΈμΆμ, ν¨μ νλΌλ―Έν°, ν¨μ κ²°κ³Ό

## λλ²κΉ (debugging)

- `print` ν¨μ νμ©
  - νΉμ  ν¨μ κ²°κ³Ό, λ°λ³΅/μ‘°κ±΄ κ²°κ³Ό λ± λλ μ μκ°, μ½λλ₯Ό bisectionμΌλ‘ λλ μ μκ°
- κ°λ° νκ²½ (text editor, IDE) λ±μμ μ κ³΅νλ κΈ°λ₯ νμ©
  - breakpoint, λ³μ μ‘°ν λ±
- Python tutor νμ© (λ¨μ νμ΄μ¬ μ½λμΈ κ²½μ°)
- λμ»΄νμΌ, λλλ²κΉ

> μ½λλ₯Ό μμ±νλ€κ°..

- μλ¬ λ©μμ§κ° λ°μνλ κ²½μ°
  - ν΄λΉ νλ μμΉλ₯Ό μ°Ύμ λ©μμ§λ₯Ό ν΄κ²°
- λ‘μ§ μλ¬κ° λ°μνλ κ²½μ°
  - λͺμμ μΈ μλ¬ λ©μμ§ μμ΄ μμκ³Ό λ€λ₯Έ κ²°κ³Όκ° λμ¨ κ²½μ°
    - μ μμ μΌλ‘ λμνμλ μ½λ μ΄ν μμ±λ μ½λλ₯Ό μκ°ν΄λ΄
    - μ μ²΄μ½λλ₯Όμ΄ν΄λ΄
    - ν΄μμκ°μ Έλ΄
    - λκ΅°κ°μκ² μ€λͺν΄λ΄
    - ...

## μλ¬μ μμΈ

### λ¬Έλ² μλ¬ (Syntax Error)

- `SyntaxError`κ° λ°μνλ©΄, νμ΄μ¬ νλ‘κ·Έλ¨μ μ€νμ΄ λμ§ μμ

- νμΌμ΄λ¦, μ€λ²νΈ, `^` λ¬Έμλ₯Ό ν΅ν΄ νμ΄μ¬μ΄ μ½λλ₯Ό μ½μ΄ λκ° λ(parser) λ¬Έμ κ° λ°μν μμΉλ₯Ό νν

- μ€μμ μλ¬κ° κ°μ§λ κ°μ₯ μμ μμΉλ₯Ό κ°λ¦¬ν€λ μΊλΏ(caret)κΈ°νΈ(^)λ₯Ό νμ

  ```python
  File "<ipython-input-1-f8a097d0a685>", line 1 
  if else ^
  SyntaxError: invalid syntax
  ```

- `EOL (End of Line)`

  λ°μ΄νλ₯Ό μμ μμ κ²½μ°

  ```python
  print('hello
  # File "<ipython-input-6-2a5f5c6b1414>", line 1 # print('hello
  #							^
  # SyntaxError: EOL while scanning string literal
  ```

- `EOF (End of File)`

  ()κ΄νΈλ₯Ό μλ«μμ κ²½μ°

  ```python
  print(
  # File "<ipython-input-4-424fbb3a34c5>", line 1 # print(
  #			^
  # SyntaxError: unexpected EOF while parsing
  ```

- `Invalid syntax`

  :μ½λ‘ μ μμ μμ κ²½μ°

  ```python
  while
  # File "<ipython-input-7-ae84bbebe3ce>", line 1 # while
  #				^
  # SyntaxError: invalid syntax
  ```

- `assign to literal`

  μμ(literal: λ³νμ§μλ κ°)μ κ°μ ν λΉνλ €κ³  νμ κ²½μ°

  - `'a' = 3` ,`True = 3` => SyntaxError

  ```python
  5=3
  # File "<ipython-input-28-9a762f2c796b>", line 1
  # 5=3
  # ^
  # SyntaxError: cannot assign to literal
  ```

  

## μμΈ (Exception)

- μ€ν λμ€ μμμΉ λͺ»ν μν©μ λ§μ΄νλ©΄, νλ‘κ·Έλ¨ μ€νμ λ©μΆ€
  - λ¬Έμ₯μ΄λ ννμμ΄ λ¬Έλ²μ μΌλ‘ μ¬λ°λ₯΄λλΌλ λ°μνλ μλ¬
- μ€ν μ€μ κ°μ§λλ μλ¬λ€μ `μμΈ(Exception)`λΌκ³  λΆλ¦
- μμΈλ μ¬λ¬ νμ(type)μΌλ‘ λνλκ³ , νμμ΄ λ©μμ§μ μΌλΆλ‘ μΆλ ₯λ¨
  - `NameError`, `TypeError` λ±μ λ°μν μμΈ νμμ μ’λ₯(μ΄λ¦)
- λͺ¨λ  λ΄μ₯ μμΈλ `Exception Class`λ₯Ό μμλ°μ μ΄λ€μ§
- μ¬μ©μ μ μ μμΈλ₯Ό λ§λ€μ΄ κ΄λ¦¬ν  μ μμ

- `ZereDivisionError`

  0μΌλ‘ λλκ³ μ ν  λ λ°μ

  ```python
  10/0
  # ---------------
  # ZeroDivisionError Traceback (most recent call last) # ----> 1 10/0
  # ZeroDivisionError: division by zero
  ```

- `NameError`

  namespace μμ μ΄λ¦μ΄ μλ κ²½μ°

  ```python
   print(name_error)
  # ---------------------------
  # NameError Traceback (most recent call last) # ----> 1 print(name_error)
  # NameError: name 'name_error' is not defined
  ```

- `TypeError`

  νμ λΆμΌμΉ

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

  arguments λΆμ‘±

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

  arguments κ°μ μ΄κ³Ό

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

  μ²«λ²μ§Έ μΈμ νμ λΆμΌμΉ

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

  νμμ μ¬λ°λ₯΄λ κ°μ΄ μ μ νμ§ μκ±°λ μλ κ²½μ°

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
  song = {'IU': 'μ’μλ '}
  song['BTS']
  # ------
  # KeyError Traceback (most recent call last) # 1 song = {'IU': 'μ’μλ '}
  # ----> 2 song['BTS'] # KeyError: 'BTS'
  ```

- `ModulNotFoundErre`

  μ‘΄μ¬νμ§ μλ λͺ¨λμ import νλ κ²½μ°

  ```python
  import nonamed
  # ------
  # ModuleNotFoundError Traceback (most recent call last) # ----> 1 import nonamed
  # ModuleNotFoundError: No module named 'nonamed'
  ```

- `ImportError`

  Moduleμ μμΌλ μ‘΄μ¬νμ§μλ ν΄λμ€/ν¨μλ₯Ό κ°μ Έμ€λ κ²½μ°

  ```python
  from random import samp
  # ------
  # ImportError Traceback (most recent call last)
  # ----> 1 from random import samp
  # ImportError: cannot import name 'samp' from 'random'
  ```

- `IndentationError`

  Indentation(λ€μ¬μ°κΈ°)μ΄ μ μ νμ§ μλ κ²½μ°

  ```python
  for i in range(3):
  print(i)
  # File "<ipython-input-56-78291925d94f>", line 2 # print(i)
  # ^
  # IndentationError: expected an indented block
  ```

- `KeyboardInter`

  μμλ‘ νλ‘κ·Έλ¨μ μ’λ£νμμ λ

  ```python
  while True: continue
  # ------
  # KeyboardInterrupt Traceback (most recent call last) # <ipython-input-55-6a65cf439648> in <module>
  # 1 while True:
  # ----> 2 continue
  # KeyboardInterrupt:
  ```

#### νμ΄μ¬ λ΄μ₯ μμΈμ ν΄λμ€ κ³μΈ΅ κ΅¬μ‘°  (built-in-exceptions)

https://docs.python.org/ko/3/library/exceptions.html#exception-hierarchy

## μμΈ μ²λ¦¬

> tryλ¬Έ (statement) / except μ (clause)μ μ΄μ©νμ¬ μμΈ μ²λ¦¬λ₯Ό ν  μ μμ

- μλ¬κ° λ°μνμ λ λ€λ₯Έ νλμ ν  μ μλλ‘ ν¨
- **tryλ¬Έμ λ°λμ ν κ° μ΄μμ exceptλ¬Έμ΄ νμ**
- `try` λ¬Έ
  - μ€λ₯κ° λ°μν  κ°λ₯μ±μ΄ μλ μ½λλ₯Ό μ€ν
  - μμΈκ° λ°μλμ§ μμΌλ©΄, except μμ΄ μ€ν μ’λ£
- `except` λ¬Έ
  - μμΈκ° λ°μνλ©΄, except μ μ΄ μ€ν
  - μμΈ μν©μ μ²λ¦¬νλ μ½λλ₯Ό λ°μμ μ μ ν μ‘°μΉλ₯Ό μ·¨ν¨
- `else`
  - `try` λ¬Έμμ μμΈκ° λ°μνμ§ μμΌλ©΄ μ€νν¨
- `finally`
  - μμΈ λ°μ μ¬λΆμ κ΄κ³μμ΄ ν­μ μ€νν¨

### μμΈμ²λ¦¬ μμ

```python
# μ«μ μλ ₯μ λ°μμ μΆλ ₯
numbers = input('μ«μλ₯Ό μλ ₯ν΄μ£ΌμΈμ: ')
print(numbers)
try:
    if int(numbers) == 5:
        print('μ€μ€~')
    else:
        print('μ€κ° μλλλ€.')
except:
    print('μ«μλ₯Ό μλ ₯νμ§ μμμ΅λλ€.')
    
# 100μ μ¬μ©μκ° μλ ₯ν μ«μλ‘ λλ μ κ²°κ³Όλ₯Ό μΆλ ₯
number = input()
try:
    print(100/int(number))
except ZeroDivisionError as err : 
# except (ValueError, ZeroDivisionError:) νκΊΌλ²μ λ¬Άμ΄μ μμΈμ²λ¦¬ κ°λ₯
    print(err)
    print('0μΌλ‘ λλ μλ μμ΅λλ€.')
except ValueError:
    print('μ«μ νμμ μλ ₯ν΄μ£ΌμΈμ.')
except Exception:
    print('μ€λ₯') # μμμ κ°λμ΄λ―λ‘ νλ¨λΆμ μμ±ν΄μΌ νλ€.
```

- νμΌμ μ΄κ³  μ½λ μ½λλ₯Ό μμ±νλ κ²½μ°

  - νμΌ μ΄κΈ° μλ
    - νμΌ μλ κ²½μ° β βν΄λΉ νμΌμ΄ μμ΅λλ€.β μΆλ ₯ `(except)`
    - νμΌ μλ κ²½μ° β νμΌ λ΄μ©μ μΆλ ₯ `(else)`
  - ν΄λΉ νμΌ μ½κΈ° μμ μ’λ£ λ©μμ§ μΆλ ₯ `(finally)`

  ```python
  νμΌμ΄ μλ κ²½μ° 
  try:
      f = open('nooofile.txt')
  except FileNotFoundError:
      print('ν΄λΉ νμΌμ΄ μμ΅λλ€.') # μ€ν
  else:
      print('νμΌμ μ½κΈ° μμν©λλ€.') 
      print(f.read())
      print('νμΌμ λͺ¨λ μ½μμ΅λλ€.') 
      f.close()
  finally:
      print('νμΌ μ½κΈ°λ₯Ό μ’λ£ν©λλ€.') # λͺ¨λ μ€ν
      
   
  
  νμΌμ΄ μλ κ²½μ° 
  try:
      f = open('file.txt') 
  except FileNotFoundError:
      print('ν΄λΉ νμΌμ΄ μμ΅λλ€.') 
  else:
      print('νμΌμ μ½κΈ° μμν©λλ€.') # μ€ν
      print(f.read())
      print('νμΌμ λͺ¨λ μ½μμ΅λλ€.') 
      f.close()
  finally:
      print('νμΌ μ½κΈ°λ₯Ό μ’λ£ν©λλ€.') # λͺ¨λ μ€ν
  ```



## μμΈ λ°μ μν€κΈ°

### raise statement

> `raise`λ₯Ό ν΅ν΄ μμΈλ₯Ό κ°μ λ‘ λ°μ

- μλ¬λΌλ κ±Έ μλ €μ£ΌκΈ° μν¨
- `raise <ννμ> (λ©μμ§)`
  - <ννμ> : μμΈ νμ μ§μ  
    - μ£Όμ΄μ§μ§ μμ κ²½μ° νμ¬ μ€μ½νμμ νμ±νλ λ§μ§λ§ μμΈλ₯Ό λ€μ μΌμΌν΄

```python
raise
# -------
# RuntimeError Traceback (most recent call last) # ----> 1 raise
# RuntimeError: No active exception to reraise
```