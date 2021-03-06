# π ν¨μ (function)

## ν¨μ κΈ°μ΄

> len(), sum(), print()..
>
> Decomposition : κΈ°λ₯μ λΆν΄ν΄μ μ¬μ¬μ© κ°λ₯
>
> Abstraction : μΆμν, λ³΅μ‘ν λ΄μ©μ μ¨κΈ°κ³  κΈ°λ₯μ μ§μ€νμ¬ μ¬μ©ν  μ μμ (λΈλλ°μ€)

- νΉμ  κΈ°λ₯μ νλ μ½λμ μ‘°κ°(λ¬Άμ)
- νΉμ  λͺλ Ήμ μννλ μ½λλ₯Ό λ§€λ² λ€μ μμ±νμ§ μκ³ , νμ μμλ§ νΈμΆνμ¬ κ°νΈν μ¬μ©
- μ¬μ©μ ν¨μ (Custom Function)
  - κ΅¬νλμ΄ μλ ν¨μκ° μλ κ²½μ°, μ¬μ©μκ° μ§μ  ν¨μλ₯Ό μμ± κ°λ₯

```python
def function_name(parameter):
    # code block
    return returning_value
```



### ν¨μλ₯Ό μ¬μ©ν΄μΌ νλ μ΄μ 

> 1. μ½λ μ€λ³΅ λ°©μ§
>
> 2. μ¬μ¬μ© μ©μ΄

### ν¨μ κΈ°λ³Έ κ΅¬μ‘°

- μ μΈκ³Ό νΈμΆ (define & call)
- μλ ₯ (Input)
- λ²μ (Scope)
- κ²°κ³Όκ° (Output)

### μ μΈκ³Ό νΈμΆ

```python
def foo():
    return True
foo()

def add(x, y): 
    return x + y
add(2, 3)
```

- ν¨μμ μ μΈμ `def` ν€μλλ₯Ό νμ©ν¨
- λ€μ¬μ°κΈ°λ₯Ό ν΅ν΄ `Function body` (μ€νλ  μ½λ λΈλ‘)λ₯Ό μμ±ν¨
  - Docstringμ ν¨μ body μμ μ νμ μΌλ‘ μμ± κ°λ₯
    - μμ±μμλ λ°λμ μ²«λ²μ§Έ λ¬Έμ₯μ λ¬Έμμ΄ ''' '''
- ν¨μλ `parameter`λ₯Ό λκ²¨μ€ μ μμ
- ν¨μλ λμ νμ `return`μ ν΅ν΄ κ²°κ³Όκ°μ μ λ¬ν¨
- ν¨μλ `ν¨μλͺ()`μΌλ‘ νΈμΆ
  - `parameter`κ° μλ κ²½μ°, `ν¨μλͺ(κ°1,κ°2,...)`λ‘ νΈμΆ

```python
# μ μ
# 1. def
# 2. Input : a, b
def add(a, b):
    # 4. return : κ°μ λ°ν
    return a + b
# νΈμΆ
print(add(5, 10))

# λ΄μ₯ ν¨μ νΈμΆ
print(sum([1, 2, 3]))
```

```python
num1 = 0
num2 = 1
def func1(a, b):
    return a + b
def func2(a, b): return a - b
def func3(a, b):
    return func1(a, 5) + func2(5, b)
result = func3(num1, num2)
print(result)
# 9
```

- ν¨μλ νΈμΆλλ©΄ μ½λλ₯Ό μ€ννκ³  `return` κ°μ λ°ννλ©° μ’λ£λλ€.



## ν¨μμ κ²°κ³Όκ° (Output)

### return

- **ν¨μλ λ°λμ κ°μ νλλ§ `return`νλ€.**
  - λͺμμ μΈ `return`μ΄ μλ κ²½μ°μλ `None`μ λ°ννλ€.
- ν¨μλ `return`κ³Ό λμμ μ€νμ΄ μ’λ£λλ€.
- νν λ°ν
  - ν¨μλ x, yμΈμλ‘ λ°κ³  νλμ `tuple`λ‘ λ°ννλ€.
  - `print()`λ `None type`μ΄λ€.

```python
def minus_and_product(x, y):
    return x - y
    return x * y
minus_and_product(4, 5) # x - yλ§ μ€νλλ€.

def minus_and_product(x, y): 
    return x - y, x * y
minus_and_product(4, 5) # (-1, 20) ννλ‘ λ°νλ¨.
```

```python
def foo():
    return 1, 2

result = foo()
print(result, type(result)) 
# (1, 2) <class 'tuple'> 

def no():
    a = 1

result = no() 
print(result, type(result)) 
# None <class 'NoneType'>


# print ν¨μλ 
# μΆλ ₯μ ν΄μ£Όκ³ , return κ°μ μμ΅λλ€. (None)
a = print('hi')
print(a, type(a)) # None <class 'NoneType'>
```



## ν¨μμ μλ ₯ (Input)

- `Parameter` : ν¨μλ₯Ό μ€νν  λ, ν¨μ λ΄λΆμμ μ¬μ©λλ μλ³μ
- `Argument` : ν¨μλ₯Ό νΈμΆν  λ, λ£μ΄μ£Όλ κ°

### argument

- ν¨μ νΈμΆ μ ν¨μμ `parameter`λ₯Ό ν΅ν΄ μ λ¬λλ κ°
- `Argument`λ μκ΄νΈ μμ ν λΉ `func_name(argument)`
- `νμ Argument` : λ°λμ μ λ¬λμ΄μΌ νλ argument
- `μ ν Argument` : κ°μ μ λ¬νμ§ μμλ λλ κ²½μ°λ κΈ°λ³Έ κ°μ΄ μ λ¬

#### positional arguments

- κΈ°λ³Έμ μΌλ‘ ν¨μ νΈμΆ μ `Argument`λ μμΉμ λ°λΌ ν¨μ λ΄μ μ λ¬λ¨

```python
def add(x, y):
  return x + y

add(2, 3)# 2μ μμΉ x, 3μ μμΉ y
```

#### keyword arguments

- μ§μ  λ³μμ μ΄λ¦μΌλ‘ νΉμ  Argumentλ₯Ό μ λ¬ν  μ μμ
- `Keyword Argument` λ€μμ `Positional Argument`λ₯Ό νμ©ν  μ μμ

```python
def add(x, y):
  return x + y

add(x=2, y=5)
add(2, y=5)
# add(x=2, 5) μλ¨
# add(y=5, x=2) λ¨
```

#### Defult Arguments Values

- κΈ°λ³Έκ°μ μ§μ νμ¬ ν¨μ νΈμΆ μ `argument` κ°μ μ€μ νμ§ μλλ‘ ν¨
  - μ μλ κ² λ³΄λ€ λ μ μ κ°μμ `argument`λ€λ‘ νΈμΆ λ  μ μμ

```python
def add(x, y=0):
  return x + y

add(2)
```

#### μ ν΄μ§μ§ μμ κ°μμ arguments

- μ¬λ¬ κ°μ `Positional Argument`λ₯Ό νλμ νμ `parameter`λ‘ λ°μμ μ¬μ©
  - λͺ κ°μ `Positional Argument`λ₯Ό λ°μμ§ λͺ¨λ₯΄λ ν¨μλ₯Ό μ μν  λ μ μ© 
- `Argument`λ€μ ννλ‘ λ¬Άμ¬ μ²λ¦¬λλ©°, `parameter`μ `*`λ₯Ό λΆμ¬ νν

```python
def add(*args):
  for args in args:
    print(arg)
    
add(2)
add(2, 3, 4, 5) # tuple type
```

#### μ ν΄μ§μ§ μμ κ°μμ keyword arguments

- ν¨μκ° μμμ κ°μ `Argument`λ₯Ό `Keyword Argument`λ‘ νΈμΆλ  μ μλλ‘ μ§μ 
- `Argument`λ€μ λμλλ¦¬λ‘ λ¬Άμ¬ μ²λ¦¬λλ©°, `parameter`μ `**`λ₯Ό λΆμ¬ νν

```python
def family(**kwargs):
  for key, value in kwargs:
    print(key, ":", value)
    
family(father='John', mother='Jane', me='Jone Jr.')
```

```python
# κΈ°λ³Έκ°μ΄ sepλ ' 'μΌλ‘ μ μκ° λμ΄ μμ.
print('hi', 'hello') # hi hello
# ν€μλλ‘ sepλ₯Ό λ°κΏμ νΈμΆν  μ μμ
print('hi', 'hello', sep='-') # hi-hello
print(1, 2, 3, 4, 5, 6, 7, 8)

# μ ν΄μ§μ§ μμ κ°―μμ μΈμ
def my_add(*numbers):
    # λ΄λΆμ μΌλ‘ numbersκ° tuple
    return numbers 

result = my_add(1, 2, 3)
print(result, type(result)) # (1, 2, 3) <class 'tuple'>

def my_func(**kwargs):
    return kwargs

result = my_func(name='νκΈΈλ', age='100', gender='M')
print(result, type(result)) # {'name': 'νκΈΈλ', 'age': '100', 'gender': 'M'} <class 'dict'>
```



## ν¨μμ λ²μ (Scope)

- ν¨μλ μ½λ λ΄λΆμ local scopeλ₯Ό μμ±νλ©°, κ·Έ μΈμ κ³΅κ°μΈ global scopeλ‘ κ΅¬λΆ
- scope
  - global scope : μ½λ μ΄λμμλ  μ°Έμ‘°ν  μ μλ κ³΅κ°
  - local scope : ν¨μκ° λ§λ  scope. ν¨μ λ΄λΆμμλ§ μ°Έμ‘° κ°λ₯
- variable
  - global variable : global scopeμ μ μλ λ³μ
  - local variable : local scopeμ μ μλ λ³μ

```python
def foo():
    a = 1 # local scope
foo()
print(a) # global scope
# NameError : name 'a' is not defined
# ν¨μ μμλ λ³μ aκ° μμ§λ§ κΈλ‘λ² κ³΅κ°μλ μμ΄μ λ³μ aλ μ μλμ§ μμλ€κ³  λμ΄
```

### κ°μ²΄ μλͺμ£ΌκΈ°

- κ°μ²΄λ κ°μμ μλͺμ£ΌκΈ°(lifecycle)κ° μ‘΄μ¬
- built-inscope
  - νμ΄μ¬μ΄ μ€νλ μ΄νλΆν° μμν μ μ§
    - `print, sum, len...`
- globalscope
  - λͺ¨λμ΄ νΈμΆλ μμ  μ΄ν νΉμ μΈν°νλ¦¬ν°κ° λλ  λκΉμ§ μ μ§
    - `a = 3`
- local scope
  - ν¨μκ° νΈμΆλ  λ μμ±λκ³ , ν¨μκ° μ’λ£λ  λκΉμ§ μ μ§
    - `def ... a = 1`

### μ΄λ¦ κ²μ κ·μΉ (Name Resolution)

- νμ΄μ¬μμ μ¬μ©λλ μ΄λ¦(μλ³μ)λ€μ μ΄λ¦κ³΅κ°(namespace)μ μ μ₯λμ΄ μμ
- μλμ κ°μ μμλ‘ μ΄λ¦μ μ°Ύμλκ°λ©°, LEGB Ruleμ΄λΌκ³  λΆλ¦
  - `Local scope` : ν¨μ
  - `Enclosed scope` : νΉμ  ν¨μμ μμ ν¨μ
  - `Global scope` : ν¨μ λ°μ λ³μ, Import λͺ¨λ
  - `Built-inscope` : νμ΄μ¬ μμ λ΄μ₯λμ΄ μλ ν¨μ λλ μμ±
- μ¦, ν¨μ λ΄μμλ λ°κΉ₯ Scopeμ λ³μμ μ κ·Ό κ°λ₯νλ μμ μ ν  μ μμ

```python
print(sum)
print(sum(range(2)))
sum = 5
print(sum)
print(sum(range(2)))

# TypeError TraceBack(most recent call last)
# 3 sum = 5
# 4 print(sum)---->
# 5 print(sum(range(2)))
# TypeError: 'int' object is not callable

sum = 5
print(sum([1, 2, 3]))

# sumμ΄ μ§κΈμ 5κ° λμ΄λ²λ¦Ό...
# Built-in scopeμ sum ν¨μκ° μμμ.
# Global scopeμ sumμ΄λ¦μ λ³μλ₯Ό λ§λ€μμ.
# μ κ° μ°ΎμΌλκΉ L->E->G->B
```

- λ³μ ν¨μμ λ£κ³ μΆμΌλ©΄ ν¨μ λ΄λΆμ μΌλ‘ λ£κ±°λ μμ μΈμλ₯Ό λ§λ€κΈ°

## ν¨μ μμ©

### λ΄μ₯ ν¨μ μμ©

- νμ΄μ¬ μΈν°νλ¦¬ν°μλ μ¬μ©ν  μ μλ λ§μ ν¨μμ ν(type)μ΄ λ΄μ₯λμ΄ μμ

### map

- map(function, iterable)

  - μν κ°λ₯ν λ°μ΄ν°κ΅¬μ‘°(iterable)μ λͺ¨λ  μμμ ν¨μ(function)μ μ©νκ³ , κ·Έ κ²°κ³Όλ₯Ό map objectλ‘ λ°ν

  - νΉμ ν ν¨μλ₯Ό λ°λ³΅μ μΌλ‘ μ μ© νκ³  μΆμ λ μ¬μ©

```python
numbers = ['1', '2', '3']
new_numbers_2 = map(int, numbers)
print(new_numbers_2, type(new_numbers_2)) 
# <map object at 0x0000023BE69A2C70> : μ΄λ―Έ ν¨μκ° λͺ¨λ μ μ©λ¨
print(list(new_numbers_2)) 
#[1, 2, 3] λ¦¬μ€νΈ νλ³νμ ν΅ν΄ κ²°κ³Ό μ§μ  νμΈ κ°λ₯

```

```python
n, m = map(int, input().split())
print(n*m)
#int() = λ΄μ₯ ν¨μ
#input() = νμ : ν­μ string(λ¬Έμμ΄)
#λ¬Έμμ΄.split() = νμ : ν­μ list(λ¦¬μ€νΈ) λ΄κ° κ΅¬λΆκ°μ κΈ°μ€μΌλ‘ μͺΌκ°κ² λ€.
#λ¬Έμμ΄λ‘ λ°μ κ²μ κ°κ°μ κ³΅λ°±μ κΈ°μ€μΌλ‘ λ¦¬μ€νΈλ‘ μͺΌκ°°λ€! -> λ¦¬μ€νΈ! ['10', '20']

#map() = μ΄λ€ ν¨μλ₯Ό λ°λ³΅κ°λ₯ν κ²λ€μ μμμ λͺ¨λ μ μ©μν¨ κ²°κ³Ό!

#int ν¨μλ₯Ό input().split() λ¦¬μ€νΈμ λͺ¨λ  μμμ μ μ©ν κ²°κ³Ό -> map object [10, 20]
#n, m = [10, 20]
```

### end =

- `print()`λ κΈ°λ³Έ `end = '\n'`μ΄λ―λ‘ print μΆλ ₯μ΄ λ μ΄ν λ€μ λ­λ₯Ό λΆμ΄κ³  μΆμ λ, κ°νμ μμ κ³  μΆμ λ (`end = ''`)



## μ°Έκ³  μλ£

[νμ΄μ¬ μμ΅μ](https://docs.python.org/ko/3/tutorial/index.html)

[νμ΄μ¬ νμ€ λΌμ΄λΈλ¬λ¦¬](https://docs.python.org/ko/3/library/index.html)