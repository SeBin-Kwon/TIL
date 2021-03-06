# ๐ ๋ฐ์ดํฐ ๊ตฌ์กฐ (Data Structure)

ํจ์ (function)

>  input()**.split()** => **๋ฌธ์์ด.split()**
>
> [1, 2, 3]**.append(4)** => **๋ฆฌ์คํธ.append(4)**

`(๋ฐ์ดํฐ)ํ์ . ๋ฉ์๋()`

## ๋ฉ์๋ (methods)

```python
# ๋ฆฌ์คํธ ๋ฉ์๋ ํ์ฉ
a = [10, 1, 100]
# ์ ๋ ฌ(sort)
new_a = a.sort()
print(a, new_a)
# [1, 10, 100] None
# ๋ฆฌ์คํธ ๋ฉ์๋๋ฅผ ํ์ฉํ๋ฉด, ๊ทธ ๋ฉ์๋๋ฅผ ์ ๋ ฌ๋ ์ํ๋ก ๋ณ๊ฒฝ(์๋ณธ ๋ณ๊ฒฝ)
# return๋๋ ๊ฒ์ None

# ๋ฆฌ์คํธ์ sorted ํจ์๋ฅผ ํ์ฉ
a = [10, 1, 100]
# ์ ๋ ฌ(sort)
new_b = sorted(b)
print(b, new_b)
#[10, 1, 100] [1, 10, 100]
# sorted ํจ์๋ฅผ ํ์ฉํ๋ฉด, ์๋ณธ์ ๋ณ๊ฒฝํ์ง ์์
# return๋๋ ๊ฒ์ ์ ๋ ฌ๋ ๋ฆฌ์คํธ

# ์ค์  ํ์ฉ ์ฝ๋
a = [10, 1, 100]
a.sort()
# a๋ฅผ ์ ๋ ฌ๋ ์ํ๋ก ํ์ฉ

b = [10, 1, 100]
b = sorted(b)
# b๋ฅผ ์ ๋ ฌ๋ ์ํ๋ก ํ์ฉ
```

## ์ํ์ค (์์๊ฐ ์๋ ๋ฐ์ดํฐ ๊ตฌ์กฐ)

## ๋ฌธ์์ด(String Type)

### ๋ฌธ์์ด ํ์/๊ฒ์ฆ

| ๋ฌธ๋ฒ         | ์ค๋ช                                                         |
| ------------ | ------------------------------------------------------------ |
| s.find(x)    | x์ ์ฒซ ๋ฒ์งธ ์์น๋ฅผ ๋ฐํ. ์์ผ๋ฉด, -1์ ๋ฐํ                   |
| s.index(x)   | x์ ์ฒซ ๋ฒ์งธ ์์น๋ฅผ ๋ฐํ. ์์ผ๋ฉด, ์ค๋ฅ ๋ฐ์                   |
| s.isalpha()  | ์ํ๋ฒณ ๋ฌธ์ ์ฌ๋ถ, ๋จ์ ์ํ๋ฒณ์ด ์๋ ์ ๋์ฝ๋ ์ Letter (ํ๊ตญ์ด๋ ํฌํจ) |
| s.isupper()  | ๋๋ฌธ์ ์ฌ๋ถ                                                  |
| s.islower()  | ์๋ฌธ์ ์ฌ๋ถ                                                  |
| s.istitile() | ํ์ดํ ํ์ ์ฌ๋ถ                                             |

#### ๋ฌธ์์ด ํ์

- `.find(x)`
  
  - x์ ์ฒซ ๋ฒ์งธ ์์น๋ฅผ ๋ฐํ. ์์ผ๋ฉด, -1์ ๋ฐํํจ.
  
  ```python
  print('apple'.find('p')) # 1 
  print('apple'.find('k')) # -1
  ```
  
- `.index(x)`
  - x์ ์ฒซ ๋ฒ์งธ ์์น๋ฅผ ๋ฐํ. ์์ผ๋ฉด, ์ค๋ฅ ๋ฐ์
  
  ```python
  print('apple'.index('pโ))
  # 1
  'apple'.index('k')
  # -------------------------------------------
  # ValueError Traceback (most recent call last)
  # ----> 1 'apple'.index('k')
  # ValueError: substring not found
  ```

#### ๋ฌธ์์ด ๊ด๋ จ ๊ฒ์ฆ ๋ฉ์๋

```python
print('abc'.isalpha()) # True 
print('Ab'.isupper()) # False 
print('ab'.islower()) # True
print('Title Title!'.istitle()) # True ์์๊ฐ ๋๋ฌธ์์ธ ๊ฒ์ด ํ์ดํ

# ์ํ๋ฒณ์ธ์ง ๊ฒ์ฆ
.isupper() # ๋๋ฌธ์?
```

- `.isdecimal()` โ `.isdigit()` โ `.isnumeric()`
  - ์ซ์์ธ์ง ๊ฒ์ฆํ๋ ค๋ฉด .`isdecimal()` ์ฐ๊ธฐ

### ๋ฌธ์์ด ๋ณ๊ฒฝ

| ๋ฌธ๋ฒ                                 | ์ค๋ช                                       |
| ------------------------------------ | ------------------------------------------ |
| **s.replace(*old, new[,count]*)**    | ๋ฐ๊ฟ ๋์ ๊ธ์๋ฅผ ์๋ก์ด ๊ธ์๋ก ๋ฐ๊ฟ์ ๋ฐํ |
| **s.strip(*[chars]*)**               | ๊ณต๋ฐฑ์ด๋ ํน์  ๋ฌธ์๋ฅผ ์ ๊ฑฐ                  |
| **s.split(*sep=None, maxsplit=-1*)** | ๊ณต๋ฐฑ์ด๋ ํน์  ๋ฌธ์๋ฅผ ๊ธฐ์ค์ผ๋ก ๋ถ๋ฆฌ         |
| **'*separator*'.join(*[iterable]*)** | ๊ตฌ๋ถ์๋ก iterable์ ํฉ์นจ                   |
| s.capitalize()                       | ๊ฐ์ฅ ์ฒซ ๋ฒ์งธ ๊ธ์๋ฅผ ๋๋ฌธ์๋ก ๋ณ๊ฒฝ          |
| s.title()                            | '๋ ๊ณต๋ฐฑ ์ดํ๋ฅผ ๋๋ฌธ์๋ก ๋ณ๊ฒฝ              |
| s.upper()                            | ๋ชจ๋ ๋๋ฌธ์๋ก ๋ณ๊ฒฝ                         |
| s.lower()                            | ๋ชจ๋ ์๋ฌธ์๋ก ๋ณ๊ฒฝ                         |
| s.swapcase()                         | ๋โ ์๋ฌธ์ ์๋ก ๋ณ๊ฒฝ                       |

- `.replace(old, new[,count])`

  - **๋ฐ๊ฟ ๋์ ๊ธ์๋ฅผ ์๋ก์ด ๊ธ์๋ก ๋ฐ๊ฟ์ ๋ฐํ**
  - count๋ฅผ ์ง์ ํ๋ฉด, ํด๋น ๊ฐ์๋งํผ๋ง ์ํ, ์ ํ ์ฌํญ

  ```python
  print('coone'.replace('o', 'a')) # caane
  print('wooooowoo'.replace('o', '!', 2)) # w!!ooowoo
  ```

- `.strip([chars])`

  - ํน์ ํ ๋ฌธ์๋ค์ ์ง์ ํ๋ฉด,
  - **์์ชฝ์ ์ ๊ฑฐํ๊ฑฐ๋(`strip`)**, ์ผ์ชฝ์ ์ ๊ฑฐํ๊ฑฐ๋(lstrip), ์ค๋ฅธ์ชฝ์ ์ ๊ฑฐ(rstrip)
    - **๋ฌธ์์ด์ ์ง์ ํ์ง ์์ผ๋ฉด ๊ณต๋ฐฑ์ ์ ๊ฑฐํจ(`space`, `\n`)**


  ```python
  print(' ์์ฐ!\n'.strip()) # '์์ฐ!'
  print(' ์์ฐ!\n'.lstrip()) # '์์ฐ!\n'
  print(' ์์ฐ!\n'.rstrip()) # ' ์์ฐ!'
  print('์๋ํ์ธ์????'.rstrip('?')) # '์๋ํ์ธ์'
  ```

- `.split(sep = None, maxsplit = -1)`

  - ๋ฌธ์์ด์ ํน์ ํ ๋จ์๋ก ๋๋  **๋ฆฌ์คํธ๋ก ๋ฐํ**
    - `sep`์ด `None`์ด๊ฑฐ๋ ์ง์ ๋์ง ์์ผ๋ฉด ์ฐ์๋ ๊ณต๋ฐฑ๋ฌธ์๋ฅผ ๋จ์ผํ ๊ณต๋ฐฑ๋ฌธ์๋ก ๊ฐ์ฃผํ๊ณ , ์ ํ/ํํ ๊ณต๋ฐฑ์ ๋น ๋ฌธ์์ด์ ํฌํจ์ํค์ง ์์.
    - `maxsplit`์ด`-1`์ธ๊ฒฝ์ฐ์๋์ ํ์ด์์.

  ```python
  print('a,b,c'.split('_')) # ['a,b,c']
  print('a b c'.split()) # ['a', 'b', 'c']
  ```

- `'separator'.join([iterable])`

  - ๋ฐ๋ณต๊ฐ๋ฅํ(iterable) ์ปจํ์ด๋ ์์๋ค์ separator(๊ตฌ๋ถ์)๋ก ํฉ์ณ **๋ฌธ์์ด ๋ฐํ**
    - **iterable์ ๋ฌธ์์ด์ด ์๋ ๊ฐ์ด ์์ผ๋ฉด TypeError ๋ฐ์**

  ```python
  print(''.join(['3', '5'])) # 35
  ```

```python
names = ','.join(['ํ๊ธธ๋', '๊น์ฒ ์'])
print(names)
# ํ๊ธธ๋, ๊น์ฒ ์

numbers = ' '.join([10, 20, 100])
print(numbers)
# TypeError: sequence item 0: expected str instance, int found

numbers = ' '.join(map(str,[10, 20, 100]))
# 10 20 100
```

### ๊ธฐํ ๋ณ๊ฒฝ

- ๋ฌธ์์ด ๋ณ๊ฒฝ ์์

  ```python
  msg = 'hI! Everyone.'
  print(msg) # hI! Everyone.
  print(msg.capitalize()) # Hi! everyone.
  print(msg.title()) # Hi! Everyone.
  print(msg.upper()) # HI! EVERYONE.
  print(msg.lower()) # hi! everyone.
  print(msg.swapcase()) # Hi! eVERYONE.
  ```

  - ๋ฌธ์์ด์ `inmutable`์ด๊ธฐ ๋๋ฌธ์(ex: ํํ, ๋ ์ธ์ง) ์ค์ค๋ก ๋ฐ๋๋ ๊ฒฝ์ฐ๊ฐ ์๋ค.

    ๋ชจ๋ ๋ฐ๋ ๊ฒฐ๊ณผ๋ฅผ ๋ฐํํ๋ค.

## ๋ฆฌ์คํธ (list)

- ๋ณ๊ฒฝ ๊ฐ๋ฅํ ๊ฐ๋ค์ ๋์ด๋ ์๋ฃํ
- ์์๋ฅผ ๊ฐ์ง๋ฉฐ, ์๋ก ๋ค๋ฅธ ํ์์ ์์๋ฅผ ๊ฐ์ง ์ ์์

- **๋ณ๊ฒฝ ๊ฐ๋ฅํ๋ฉฐ(mutable)**, ๋ฐ๋ณต ๊ฐ๋ฅํจ(iterable)
- ํญ์ ๋๊ดํธ ํํ๋ก ์ ์ํ๋ฉฐ, ์์๋ ์ฝค๋ง๋ก ๊ตฌ๋ถ `[ 0,1,2,3,4,5 ]`

| ๋ฌธ๋ฒ                   | ์ค๋ช                                                         |
| ---------------------- | ------------------------------------------------------------ |
| **L.append(x)**        | ๋ฆฌ์คํธ ๋ง์ง๋ง์ ํญ๋ชฉ x๋ฅผ ์ถ๊ฐ                                |
| **L.insert(i, x)**     | ๋ฆฌ์คํธ ์ธ๋ฑ์ค i์ ํญ๋ชฉ x๋ฅผ ์ฝ์                              |
| **L.remove(x)**        | ๋ฆฌ์คํธ ๊ฐ์ฅ ์ผ์ชฝ์ ์๋ ํญ๋ชฉ(์ฒซ ๋ฒ์งธ) x๋ฅผ ์ ๊ฑฐ, ํญ๋ชฉ์ด ์กด์ฌํ์ง ์์ ๊ฒฝ์ฐ, ValueError |
| **L.pop()**            | ๋ฆฌ์คํธ ๊ฐ์ฅ ์ค๋ฅธ์ชฝ์ ์๋ ํญ๋ชฉ(๋ง์ง๋ง)์ ๋ฐํ ํ ์ ๊ฑฐ        |
| **L.pop(i)**           | ๋ฆฌ์คํธ์ ์ธ๋ฑ์ค i์ ์๋ ํญ๋ชฉ์ ๋ฐํ ํ ์ ๊ฑฐ                 |
| L.extend(m)            | ์ํํ m์ ๋ชจ๋  ํญ๋ชฉ๋ค์ ๋ฆฌ์คํธ ๋์ ์ถ๊ฐ (+=๊ณผ ๊ฐ์ ๊ธฐ๋ฅ)   |
| L.index(x, start, end) | ๋ฆฌ์คํธ์ ์๋ ํญ๋ชฉ ์ค ๊ฐ์ฅ ์ผ์ชฝ์ ์๋ ํญ๋ชฉ x์ ์ธ๋ฑ์ค๋ฅผ ๋ฐํ |
| L.reverse()            | ๋ฆฌ์คํธ๋ฅผ ๊ฑฐ๊พธ๋ก ์ ๋ ฌ                                         |
| **L.sort()**           | ๋ฆฌ์คํธ๋ฅผ ์ ๋ ฌ (๋งค๊ฐ๋ณ์ ์ด์ฉ๊ฐ๋ฅ)                            |
| **L.count(x)**         | ๋ฆฌ์คํธ์์ ํญ๋ชฉ x๊ฐ ๋ช ๊ฐ ์กด์ฌํ๋์ง ๊ฐฏ์๋ฅผ ๋ฐํ             |

### ๊ฐ ์ถ๊ฐ ๋ฐ ์ญ์ 

- **`.append(x)`**

  - ๋ฆฌ์คํธ์ ๊ฐ์ ์ถ๊ฐํจ (๋งจ ๋ค์ ์ถ๊ฐ๋จ)

  ```python
  cafe = ['starbucks', 'tomntoms', 'hollys'] print(cafe)
  # ['starbucks', 'tomntoms', 'hollys'] cafe.append('banapresso')
  print(cafe)
  # ['starbucks', 'tomntoms', 'hollys', 'banapresso']
  ```

```python
a = [1, 2, 3]
a = a.append(4)
print(a) # None
# a.append(4)์ return ๊ฐ์ a์ ์ ์ฅํ๋ค.
# ๋ฆฌ์คํธ.append()์ ๋ฉ์๋๋ ๋ฐํ๊ฐ์ด None์!

a = [1, 2, 3]
a.append(4) 
print(a) # [1, 2, 3, 4]
```

- `.extend (iterable)`

  - ๋ฆฌ์คํธ์ `iterable`์ ํญ๋ชฉ์ ์ถ๊ฐํจ

  - ๋ฐ๋์ ๋ฆฌ์คํธ๋ก ํ๋๋ก ๋ฌถ์ด์ผํจ

  - ๋ฌธ์์ด์ `input`ํ๋ฉด ๋จ์ด ํ๋ํ๋ ๋ฐํ


  ```python
  cafe = ['starbucks', 'tomntoms', 'hollys']
  print(cafe)
  # ['starbucks', 'tomntoms', 'hollys']
  cafe.extend(['cafe', 'test'])
  print(cafe)
  # ['starbucks', 'tomntoms', 'hollys', 'cafe', 'test]
  
  a = ['apple']
  a.extend(['banana', 'mango'])
  print(a) 
  # ['apple', 'banana', 'mango']
  
  a.extend('banana')
  print(a)
  # ['apple', 'banana', 'mango', 'b', 'a', 'n', 'a', 'n', 'a']
  ```

- `.insert(i,x)`

  - ์ ํด์ง ์์น i์ ๊ฐ์ ์ถ๊ฐํจ

  ```python
  cafe = ['starbucks', 'tomntoms'] 
  print(cafe)
  # ['starbucks', 'tomntoms'] 
  cafe.insert(0, 'start') 
  print(cafe)
  # ['start', 'starbucks', 'tomntoms']
  
  cafe = ['starbucks', 'tomntoms']
  print(cafe)
  # ['starbucks', 'tomntoms']
  cafe.insert(10000, 'end') # ๋ฆฌ์คํธ ๊ธธ์ด๋ณด๋ค ํฐ ๊ฒฝ์ฐ ๋งจ ๋ค์ ์ถ๊ฐํจ
  print(cafe)
  # ['starbucks', 'tomntoms', 'end']
  ```

- `.remove(x)`

  - ๋ฆฌ์คํธ์์ ๊ฐ์ด x์ธ ๊ฒ ์ญ์ 

  ```python
  numbers = [1, 2, 3, 'hi'] 
  print(numbers) # [1, 2, 3, 'hi'] 
  numbers.remove('hi') 
  print(numbers) # [1, 2, 3]
  
  numbers.remove('hi') # ์๋ ๊ฒฝ์ฐ ValueError
  # ----------------
  # ValueError Traceback (most recent call last) # ----> 1 numbers.remove('hi')
  # ValueError: list.remove(x): x not in list
  ```

- `.pop(i)`

  - ์ ํด์ง ์์น i์ ์๋ ๊ฐ์ ์ญ์ ํ๊ณ , ๊ทธ ํญ๋ชฉ์ ๋ฐํํจ
  - i๊ฐ ์ง์ ๋์ง ์์ผ๋ฉด, ๋ง์ง๋ง ํญ๋ชฉ์ ์ญ์ ํ๊ณ  ๋ฐํํจ

  ```python
  numbers = ['hi', 1, 2, 3] 
  # ['hi', 1, 2, 3] 
  pop_number = numbers.pop() 
  print(pop_number)
  #3
  print(numbers)
  # ['hi', 1, 2]
  
  numbers = ['hi', 1, 2, 3] 
  # ['hi', 1, 2, 3] 
  pop_number = numbers.pop(0) 
  print(pop_number)
  # 'hi'
  print(numbers)
  # [1, 2, 3]
  ```

- `.clear()`

  - ๋ชจ๋  ํญ๋ชฉ์ ์ญ์ ํจ

  ```python
  numbers = [1, 2, 3] 
  print(numbers)
  # [1, 2, 3] 
  print(numbers.clear()) 
  # []
  ```

### ํ์ ๋ฐ ์ ๋ ฌ

- `.index(x)`

  - x๊ฐ์ ์ฐพ์ ํด๋น index ๊ฐ์ ๋ฐํ

  ```python
  numbers = [1, 2, 3, 4] 
  print(numbers) # [1, 2, 3, 4] 
  print(numbers.index(3)) # 2
  print(numbers.index(100)) # ์๋ ๊ฒฝ์ฐ ValueError
  # ---------------------
  # ValueError Traceback (most recent call last)
  #       2 print(numbers)
  # 3 print(numbers.index(3)) 
  # ----> 4 print(numbers.index(100))
  # ValueError: 100 is not in list
  ```

- `.count(x)`

  - ์ํ๋ ๊ฐ์ ๊ฐ์๋ฅผ ๋ฐํํจ
  - ๋ฌธ์์ด์์๋ ์ฌ์ฉ ๊ฐ๋ฅ

  ```python
  numbers = [1, 2, 3, 1, 1] 
  print(numbers.count(1)) # 3 
  print(numbers.count(100)) # 0
  ```

- `.sort()`

  - ์๋ณธ ๋ฆฌ์คํธ๋ฅผ ์ ๋ ฌํจ. None ๋ฐํ
  - `sorted` ํจ์์ ๋น๊ตํ  ๊ฒ

  ```python
  numbers = [3, 2, 5, 1]
  result = numbers.sort() 
  print(numbers, result) 
  # [1, 2, 3, 5] None
  # ์๋ณธ ๋ณ๊ฒฝ
  
  numbers = [3, 2, 5, 1] 
  result = sorted(numbers) 
  print(numbers, result)
  # [3, 2, 5, 1] [1, 2, 3, 5]
  # ์ ๋ ฌ๋ ๋ฆฌ์คํธ๋ฅผ ๋ฐํ. ์๋ณธ ๋ณ๊ฒฝ ์์

- `.reverse()`

  - ์์๋ฅผ ๋ฐ๋๋ก ๋ค์ง์ (์ ๋ ฌํ๋ ๊ฒ์ด ์๋). None ๋ฐํ

  ```python
  numbers = [3, 2, 5, 1] 
  result = numbers.reverse() 
  print(numbers, result)
  # [1, 5, 2, 3] None
  ```

```python
# ๋ฆฌ์คํธ๋ mutable
a = [1, 2, 3]
a[0] = 100
prnit(a)
#[100, 2, 3]

# ๋ฌธ์์ด์ immutable
# ๋ฌธ์์ด์ ์ฒซ๋ฒ์งธ ์ธ๋ฑ์ค์ ํด๋นํ๋ ๊ฐ์ ๋ฐ๊ฟ ์ ์๋ค.
a = 'hi'
a[0] = 'c'
print(a)
# TypeError: 'str' object does not support item assignment
```

```python
a = [1, 2, 3]
# sum(a)์ ๊ฒฐ๊ณผ(int, ํฉ ๊ณ์ฐ ๊ฒฐ๊ณผ)๋ฅผ result ํ ๋น
result = sum(a) # 6

numbers = [1, 3, 2]
result = numbers.reverse() # None์ด ๋ฐํ๋๊ณ , numbers๋ ๋ฐ๋์ด์์
# ๊ทธ๋์ ์ผ๋ฐ์ ์ผ๋ก ์ฝ๋๋
numbers.reverse()

a = ['1','2','3'].index('2')+10
print(a) # 11
# .index์ '2'๋ a๋ฆฌ์คํธ์ ์ธ๋ฑ์ค [1]์ ํด๋นํ๋ฏ๋ก ๊ฐ์ด 1์ด๋ค.
# 1 + 10 = 11
```



## ์ปฌ๋ ์ (์์๊ฐ ์๋ ๋ฐ์ดํฐ ๊ตฌ์กฐ)

## ์ธํธ (set)

- ์ ์ผํ ๊ฐ๋ค์ ๋ชจ์(collection)
- ์์๊ฐ ์๊ณ  ์ค๋ณต๋ ๊ฐ์ด ์์.
  - ์ํ์์์ ์งํฉ๊ณผ ๋์ผํ ๊ตฌ์กฐ๋ฅผ ๊ฐ์ง๋ฉฐ, ์งํฉ ์ฐ์ฐ๋ ๊ฐ๋ฅ
- ๋ณ๊ฒฝ ๊ฐ๋ฅํ๋ฉฐ(mutable), ๋ฐ๋ณต ๊ฐ๋ฅํจ(iterable)
  - ๋จ, ์ธํธ๋ ์์๊ฐ ์์ด ๋ฐ๋ณต์ ๊ฒฐ๊ณผ๊ฐ ์ ์ํ ์์์ ๋ค๋ฅผ ์ ์์

### ์ธํธ ๋ฉ์๋

| ๋ฌธ๋ฒ            | ์ค๋ช                                                         |
| --------------- | ------------------------------------------------------------ |
| s.copy()        | ์ธํธ์ ์์ ๋ณต์ฌ๋ณธ์ ๋ฐํ                                    |
| s.add(x)        | ํญ๋ชฉ x๊ฐ ์ธํธ s์ ์๋ค๋ฉด ์ถ๊ฐ                                |
| s.pop()         | ์ธํธs์์ ๋๋คํ๊ฒ ํญ๋ชฉ์ ๋ฐํํ๊ณ  ํด๋น ํญ๋ชฉ์ ์ ๊ฑฐ, ์ธํธ๊ฐ ๋น์ด ์์ ๊ฒฝ์ฐ, KeyError |
| s.remove(s)     | ํญ๋ชฉ x๋ฅผ ์ธํธ s์์ ์ญ์ , ํญ๋ชฉ์ด ์กด์ฌํ์ง ์์ ๊ฒฝ์ฐ, KeyError |
| s.discard(x)    | ํญ๋ชฉ x๊ฐ ์ธํธ s์ ์๋ ๊ฒฝ์ฐ, ํญ๋ชฉ x๋ฅผ ์ธํธs์์ ์ญ์          |
| s.update(t)     | ์ธํธ t์ ์๋ ๋ชจ๋  ํญ๋ชฉ ์ค ์ธํธ s์ ์๋ ํญ๋ชฉ์ ์ถ๊ฐ         |
| s.clear()       | ๋ชจ๋  ํญ๋ชฉ์ ์ ๊ฑฐ                                             |
| s.isdisjoint(t) | ์ธํธ s๊ฐ ์ธํธ t์ ์๋ก ๊ฐ์ ํญ๋ชฉ์ ํ๋๋ผ๋ ๊ฐ๊ณ  ์์ง ์์ ๊ฒฝ์ฐ, True๋ฐํ |
| s.issubset(t)   | ์ธํธ s๊ฐ ์ธํธ t์ ํ์ ์ธํธ์ธ ๊ฒฝ์ฐ, True๋ฐํ                 |
| s.issuperset(t) | ์ธํธ s๊ฐ ์ธํธ t์ ์์ ์ธํธ์ธ ๊ฒฝ์ฐ, True๋ฐํ                 |



## ๋์๋๋ฆฌ (Dictionary)

- ํค-๊ฐ(key-value) ์์ผ๋ก ์ด๋ค์ง ๋ชจ์(collection)

  - ํค(key)
    - ๋ถ๋ณ ์๋ฃํ๋ง ๊ฐ๋ฅ (๋ฆฌ์คํธ, ๋์๋๋ฆฌ ๋ฑ์ ๋ถ๊ฐ๋ฅํจ)
  - ๊ฐ(values)
    - ์ด๋ ํํํ๋ ๊ด๊ณ์์

- ํค์ ๊ฐ์ `:` ๋ก ๊ตฌ๋ถ๋ฉ๋๋ค. ๊ฐ๋ณ ์์๋ `,` ๋ก ๊ตฌ๋ถ๋ฉ๋๋ค.

- ๋ณ๊ฒฝ ๊ฐ๋ฅํ๋ฉฐ(mutable), ๋ฐ๋ณต ๊ฐ๋ฅํจ(iterable)

  - ๋์๋๋ฆฌ๋ ๋ฐ๋ณตํ๋ฉด ํค๊ฐ ๋ฐํ๋ฉ๋๋ค.

  ```python
  students = {'ํ๊ธธ๋': 30, '๊น์ฒ ์': 25} 
  students['ํ๊ธธ๋'] # 30
  ```

| ๋ฌธ๋ฒ                | ์ค๋ช                                                         |
| ------------------- | ------------------------------------------------------------ |
| d.clear()           | ๋ชจ๋  ํญ๋ชฉ์ ์ ๊ฑฐ                                             |
| d.keys()            | ๋์๋๋ฆฌ d์ ๋ชจ๋  ํค๋ฅผ ๋ด์ ๋ทฐ๋ฅผ ๋ฐํ                        |
| d.values()          | ๋์๋๋ฆฌ d์ ๋ชจ๋  ๊ฐ๋ฅผ ๋ด์ ๋ทฐ๋ฅผ ๋ฐํ                        |
| d.items()           | ๋์๋๋ฆฌ d์ ๋ชจ๋  ํค-๊ฐ์ ์์ ๋ด์ ๋ทฐ๋ฅผ ๋ฐํ                |
| d.get(k)            | ํค k์ ๊ฐ์ ๋ฐํํ๋๋ฐ, ํค k๊ฐ ๋์๋๋ฆฌ d์ ์์ ๊ฒฝ์ฐ None์ ๋ฐํ |
| d.get(k, v)         | ํค k์ ๊ฐ์ ๋ฐํํ๋๋ฐ, ํค k๊ฐ ๋์๋๋ฆฌ d์ ์์ ๊ฒฝ์ฐ v์ ๋ฐํ |
| d.pop(k)            | ํค k์ ๊ฐ์ ๋ฐํํ๊ณ  ํค k์ธ ํญ๋ชฉ์ ๋์๋๋ฆฌ d์์ ์ญ์ ํ๋๋ฐ, ํค k๊ฐ ๋์๋๋ฆฌ d์ ์์ ๊ฒฝ์ฐ KeyError๋ฅผ ๋ฐ์ |
| d.pop(k, v)         | ํค k์ ๊ฐ์ ๋ฐํํ๊ณ  ํค k์ธ ํญ๋ชฉ์ ๋์๋๋ฆฌ d์์ ์ญ์ ํ๋๋ฐ, ํค k๊ฐ ๋์๋๋ฆฌ d์ ์์ ๊ฒฝ์ฐ v๋ฅผ ๋ฐํ |
| d.update([*other*]) | ๋์๋๋ฆฌ d์ ๊ฐ์ ๋งคํํ์ฌ ์๋ฐ์ดํธ                          |

### ์กฐํ

- `.get(key)`

  - key๋ฅผ ํตํด value๋ฅผ ๊ฐ์ ธ์ด
  - KeyError๊ฐ ๋ฐ์ํ์ง ์์ผ๋ฉฐ, default ๊ฐ์ ์ค์ ํ  ์ ์์(๊ธฐ๋ณธ: None)

  ```python
  my_dict = {'apple': '์ฌ๊ณผ', 'banana': '๋ฐ๋๋'}
  my_dict['pineapple']
  # ------------------------------
  # KeyError Traceback (most recent call last) # 1 my_dict = {'apple': '์ฌ๊ณผ', 'banana': '๋ฐ๋๋'}
  # ----> 2 my_dict['pineappleโ]
  # KeyError: 'pineapple'
  
  my_dict = {'apple': '์ฌ๊ณผ', 'banana': '๋ฐ๋๋'} print(my_dict.get('pineapple'))
  # None
  print(my_dict.get('apple'))
  # ์ฌ๊ณผ 
  print(my_dict.get('pineapple', 0)) 
  #0 ์ ๋ณด๋ ์์ง๋ง ์กฐ์ํ๊ณ  ์ถ์ ๋ ๋ํดํธ ๊ฐ์ ์ค์ ํด๋์ ์ ์๋ค.
  ```

- `.pop(key[,default])`

  - key๊ฐ ๋์๋๋ฆฌ์ ์์ผ๋ฉด ์ ๊ฑฐํ๊ณ  ํด๋น ๊ฐ์ ๋ฐํ
  - ๊ทธ๋ ์ง ์์ผ๋ฉด default๋ฅผ ๋ฐํ
  - default๊ฐ์ด ์์ผ๋ฉด KeyError

  ```python
  my_dict = {'apple': '์ฌ๊ณผ', 'banana': '๋ฐ๋๋'} 
  data = my_dict.pop('apple')
  print(data, my_dict)
  # ์ฌ๊ณผ {'banana': '๋ฐ๋๋'}
  
  my_dict = {'apple': '์ฌ๊ณผ', 'banana': '๋ฐ๋๋'} 
  data = my_dict.pop('pineapple')
  print(data, my_dict)
  # ----------------
  # KeyError Traceback (most recent call last)
  # 1 my_dict = {'apple': '์ฌ๊ณผ', 'banana': '๋ฐ๋๋'} # ----> 2 data = my_dict.pop('pineapple')
  # 3 print(data, my_dict)
  # KeyError: 'pineapple'
  ```

- `.update([other])`

  - ๊ฐ์ ์ ๊ณตํ๋ key, value๋ก ๋ฎ์ด์๋๋ค.

  ```python
  my_dict = {'apple': '์ฌ', 'banana': '๋ฐ๋๋'} my_dict.update(apple='์ฌ๊ณผ')
  print(my_dict)
  # {โappleโ: โ์ฌ๊ณผโ, 'banana': '๋ฐ๋๋'}
  ```

```python
# ๊ธฐ๋ณธ ์ํ

my_dict = {'apple': '์ฌ๊ณผ', 'banana': '๋ฐ๋๋'}
# key๊ฐ ๊ธฐ์ค์ด๊ณ , ์ง์  ๋์๋๋ฆฌ์ key๋ก ์ ๊ทผํ๋ฉด value๋ฅผ ์ป์ ์ ์๋ค!
for word in my_dict:
    print(word, my_dict[word]) # apple ์ฌ๊ณผ # banana ๋ฐ๋๋

# ๋ค์ํ ๋ฐฉ๋ฒ
print(my_dict.keys(), type(my_dict.keys()))
# dict_keys(['apple', 'banana']) 
# ํ์ : dict_keys(์ผ์ข์ ๋ฆฌ์คํธ)

print(my_dict.values())
# dict_values(['์ฌ๊ณผ', '๋ฐ๋๋'])(์ผ์ข์ ๋ฆฌ์คํธ)

# ์์ฉ
for value in my_dict.values():
    print(value) # ์ฌ๊ณผ # ๋ฐ๋๋

print(my_dict.items())
# ์ผ์ข์ ๋ฆฌ์คํธ์์, tuple!
# dict_items([('apple', '์ฌ๊ณผ'), ('banana', '๋ฐ๋๋')])
for k, v in my_dict.items():
    print(k, v)
# apple ์ฌ๊ณผ # banana ๋ฐ๋๋

# ๋์๋๋ฆฌ์ ๊ฐ ์ถ๊ฐํ๊ธฐ
my_dict_2 = {}
my_dict_2['a'] = 'airplane'

# 1 ์ฆ๊ฐ ์ํค๊ธฐ
my_dict_3 = {'a': 0}
my_dict_3['a'] += 1 
# ํค๊ฐ 'a'์ ์ ๊ทผํ์ฌ ๋ฐธ๋ฅ 0๊ณผ 1์ ๋ํด 'a'์ ํ ๋น
print(my_dict_3)
# {'a' : 1 }

my_list = [10, 11, 12]
my_list[0] = my_list[0] + 1
# ์ธ๋ฑ์ค[0](์ฒซ๋ฒ์งธ)์ ์ ๊ทผํด 1์ ๋ํ ๊ฒ์ ์ธ๋ฑ์ค[0]์ ํ ๋น 

my_dict = {'apple': '์ฌ๊ณผ', 'banana': '๋ฐ๋๋'}
print(my_dict['apple']) # ์ฌ๊ณผ

for word in my_dict: # 'apple', 'banana' ํค๊ฐ์ด ๋์ด
    print(my_dict[word]) # ์ฌ๊ณผ , ๋ฐ๋๋ 
    # ๋์๋๋ฆฌ์ ํค๊ฐ์ ๋ฃ์ด ์ง์  ์ ๊ทผํ์ฌ ๋ฐธ๋ฅ๋ฅผ ์ป์
    
[1, 2, 3] + [4, 5] 
# [1, 2, 3, 4, 5]
{'a': 'apple'} + {'b': 'banana'}
# TypeError, unsupported operand type(s) for +: 'dict' and 'dict'

```



## ์ฐธ๊ณ  ์๋ฃ

[python tutor](https://pythontutor.com/visualize.html#mode=edit)

