# 🚀 객체 지향 프로그래밍 심화

```python
# 클래스 정의
class Person:
    pass

# 인스턴스 생성
p1 = Person()
# 인스턴스 속성
p1.name = '홍길동'

print(p1.name) # 홍길동
```

```python
class Person:
    # 클래스 변수(속성)
    species = '사람'
    
    # 인스턴스 메서드
    # 인스턴스가 활용할 메서드
    def greeting(self):
        print('안녕하세요')
        
iu = Person() 
iu.greeting() # 메서드 호출
# 안녕하세요

# 클래스 변수(속성)
print(Person.species) 
# 사람
```

> 함수는 그냥 input과 output
>
> 메서드는 클래스 내에 관리되는 함수

<br>

```python
class Person:
    # 사람이라면 이름을 가지고 있다.
    # 인스턴스를 만들 때는 이름 정보를 받아서 하고 싶다.

    # 생성자 메서드
    def__init__(self, name):
        # 개별 인스턴스에 각각 name 속성을 지정
         self.name = name
    # self : 호출하는 인스턴스를 파이썬 내부적으로 전달해줌
    def greeting(self):
        # print('안녕하세요, 지민입니다.') 개별적으로 적용할 수 없음
        print(f'안녕하세요. {self.name}입니다.')

# 인스턴스 만들 때
jimin = Person('지민')
print(jimin.name)
# 지민

jimin.greeting()
# 안녕하세요, 지민입니다.
# 내부적으로 Person.greeting(jimin) 이런 느낌으로 작동함

iu = Person('지은')
iu.greeting()
# 안녕하세요, 지은입니다.
```

<br>

```python
# 로또
import random

for i in range(5)
    numbers = range(1,46)
    result = random.samlpe(numbers, 6)
    result.sort()

    print(result)
```

```python
# 함수
import random 

# n을 넣으면 그 횟수 만큼
def generate_lotto(n):
    result = []
    for i in range(n):
        numbers = range(1,46)
        pick = random.samlpe(numbers, 6)
        pick.sort()
    return result
def check(buy_numbers, result_numbers):
    return 0
print(generate_lotto(5))
```

```python
# 모듈
import lotto_function
# 이 코드의 결과 
# 로또 번호들의 리스트
print(lotto_function.generate_lotto(5))
lotto_function.check(buy_numbers, [1, 2, 3, 4, 5, 6])
# input => output 말고는 없음
```

```python
# 클래스
import random

class Lotto:
    def generate_lotto(self):
        self.numbers = sorted(random.sample(range(1, 46), 6))

    def get_money(self, real_numbers):
        print('당신의 숫자는', self.numbers)
        print('당첨 숫자는', real_numbers)
        if self.numbers == real_numbers:
            return 10000000000
        else:
            return 0

# 유저
import lotto_class

lotto = lotto_class.Lotto()
lotto.generate_lotto()
print(lotto.numbers)
print(lotto.get_money([1, 2, 3, 4, 5, 6]))

# lotto 인스턴스로 속성 볼 수 있고(numbers), 내가 생성도 하고, 확인(get_money)도 가능하다.
```

<br>

# 🚅 클래스

- **`클래스 속성(attribute)`**

  - 한 클래스의 모든 인스턴스라도 똑같은 값을 가지고 있는 속성
  - 클래스 선언 내부에서 정의
  - `<classname>.<name>`으로 접근 및 할당

  ```python
  class Circle: 
      pi = 3. 14
      
  c1 = Circle()
  c2 = Circle()
  
  print(Circle.pi) # 3. 14
  print(c1.pi) # 3. 14
  print(c2.pi) # 3. 14
  ```

<br>

- **인스턴스와 클래스 간의 `이름 공간(namespace)`**

  - 클래스를 정의하면, 클래스와 해당하는 이름 공간 생성
  - 인스턴스를 만들면, 인스턴스 객체가 생성되고 이름 공간 생성
  - 인스턴스에서 특정 속성에 접근하면, 인스턴스-클래스 순으로 탐색

  ```python
  class Person:
      species = 'human' 
      # 클래스 이름 공간에 저장
      
      def__init__(self, name):
          self.name = name
  p1 = Person('Hong') 
  p2 = Person('Choi')
  # 인스턴트별 이름 공간에 저장
  
  class Person:
      name = 'unknown'
      def talk(self):
          print(self.name)
  p2 = Person()
  p2.talk() 
  # unknown
  # 인스턴스 이름 공간에 name이 없어 클래스 이름 공간 탐색
  p2.name = 'Kim' # 인스턴스 이름 공간에 저장
  p2.talk() 
  # Kim
  ```


<br>

- **`클래스 메소드`**

  - 클래스가 사용할 메소드
  - `@classmethod` 데코레이터를 사용하여 정의
    - 데코레이터 : 함수를 어떤 함수로 꾸며서 새로운 기능을 부여
  - 호출 시, 첫번째 인자로 클래스`(cls)`가 전달됨

  ```python
  class MyClass:
      @classmethod
      def class_method(cls, arg1, ...)
  ```

<br>

- **`스태틱 메소드`**
  - 인스턴스 변수, 클래스 변수를 전혀 다루지 않는 메소드
- **언제 사용하는가?**
  - 속성을 다루지 않고 단지 기능(행동)만을 하는 메소드를 정의할 때 사용
  - `@staticmethod` 데코레이터를 사용하여 정의
  - **호출 시, 어떠한 인자도 전달되지 않음** (클래스 정보에 접근/수정 불가)

```python
# 함수 내부에서 값을 쓰고 싶으면 어떻게 해야하죠?
# 정의할 때 이름을 지어놓고, 호출할 때 값을 넘겨줘요!

class MyClass:
    class_variable = '클래스 변수'
    
    # 메서드들을 정의했습니다.
    def__init__(self):
        self.instance_variable = '인스턴스 변수'
    # 인스턴스 메서드 정의
    def instance_variable(self):
        return self, self.instance_variable
      
    # 클래스 메서드 정의
    @classmethod
    def class_method(cls):
        return cls, cls.class_variable
    # 스태틱 메서드 정의
    @staticmethod
    def static_method():
        return '스태틱'

c1 = MyClass()
print('인스턴스 변수 호출', c1.instance_variable)
# 인스턴스 변수 호출 인스턴스 변수

print('인스턴스 메서드 호출', c1.instance_method())
# 인스턴스 메서드 호출 (<__main__.MyClass object at 0x104ee0f10>, '인스턴스 변수')

print('클래스 메서드 호출', c1.class_method())
# 클래스 메서드 호출 (<class '__main__.MyClass'>, '클래스변수')

print('스태틱 메서드 호출', c1.static_method())
# 스태틱 메서드 호출 스태틱
```

- `self`, `cls`은 관용적으로 쓰이는 것임

- 스태틱 메서드 안에 인스턴스, 클래스 메서드를 사용할 수 없다.

<br>

#### 정리

- 클래스구현
  - 클래스 정의
  - 데이터 속성 정의 (객체의 정보는 무엇인지)
  - 메소드 정의 (객체를 어떻게 사용할 것인지)
- 클래스 활용
  - 해당 객체 타입의 인스턴스 생성 및 조작

#### 메소드 정리

- `인스턴스 메소드`
  - 호출한 인스턴스를 의미하는 `self ` 매개 변수를 통해 인스턴스를 조작
- `클래스 메소드`
  - 클래스를 의미하는 `cls` 매개 변수를 통해 클래스를 조작
- `스태틱 메소드`
  - 인스턴스나 클래스를 의미하는 매개변수는 사용하지 않음
    - 즉, 객체 상태나 클래스 상태를 수정할 수 없음
  - 일반 함수처럼 동작하지만 클래스의 이름공간에 귀속 됨
    - 주로 해당 클래스로 한정하는 용도로 사용

<br>

#### 예시

```python
class MyClass:
    def method(self):
        return 'instance method', self
    @classmethod
    def classmethod(cls):
        return 'class method', cls
    @staticmethod
    def staticmethod():
        return 'static method'
```

<br>

## 객체 지향의 핵심 개념

### **객체지향의 핵심 4가지**

> 추상화, 상속, 다형성, 캡슐화

<br>

## 추상화

- 로또를 메서드를 통해 기능을 구현해서 활용할 수 있게 하는 것
- 기능 / 정보 등을 표현해 놓은 것

<br>

## 상속

- 두 클래스 사이 부모 – 자식 관계를 정립하는 것

- 클래스는 상속이 가능함

  - 모든 파이썬 클래스는 `object`를 상속 받음

  ```python
  class ChildClass(ParentClass):
      pass
  ```

- 하위 클래스는 상위 클래스에 정의된 속성, 행동, 관계 및 제약 조건을 모두 상속 받음
- 부모 클래스의 속성, 메소드가 자식 클래스에 상속되므로, 코드 재사용성이 높아짐
- 상속 관련 함수와 메소드
  - `isinstance(object, classinfo)`
    - class가 classinfo의 `instance`거나**`subclass`**인 경우 True
    - classinfo는 클래스 객체의 튜플일 수 있으며, classinfo의 모든 항목을 검사
  - `super()`
    - 자식 클래스에서 부모 클래스를 사용하고 싶은 경우

<br>

### 상속 정리

- 파이썬의 모든 클래스는 `object`로부터 상속됨
- 부모 클래스의 모든 요소(속성, 메소드)가 상속됨
- `super()`를 통해 부모 클래스의 요소를 호출할 수 있음
- 메소드 오버라이딩을 통해 자식 클래스에서 재정의 가능함
- 상속 관계에서의 이름 공간은 인스턴스, 자식 클래스, 부모 클래스 순으로 탐색

<br>

### 다중상속

- 두 개 이상의 클래스를 상속 받는 경우
- 상속 받은 모든 클래스의 요소를 활용 가능함
- 중복된 속성이나 메서드가 있는 경우 상속 순서에 의해 결정됨

<br>

## 다형성

> 다형성(Polymorphism)은 여러 모양을 뜻하는 그리스어

- 동일한 메소드가 클래스에 따라 다르게 행동할 수 있음을 의미
- 즉, 서로 다른 클래스에 속해있는 객체들이 **동일한 메시지에 대해 다른 방식으로 응답될 수 있음**

<br>

### 메소드 오버라이딩

- 상속 받은 메소드를 재정의, 메소드를 덮어씌울 수 있다.

- 클래스 상속 시, 부모 클래스에서 정의한 메소드를 자식 클래스에서 변경

- 부모 클래스의 메소드 이름과 기본 기능은 그대로 사용하지만, 특정 기능을 바꾸고 싶을 때 사용

  ```python
  class Person:
      def __init__(self, name):
          self.name = name
      def talk(self):
          print(f'반갑습니다. {self.name}입니다.')
          
  # 자식 클래스 - Professor
  class talk(self):
      print(f'{self.name}일세.')
      
  
  # 자식 클래스 - Student
  class talk(self):
      super().talk()
      print(f'저는 학생입니다.')
      
  p1 = Professor('김교수')
  p1.talk() # 김교수일세.
  
  s1 = Student('이학생')
  s1.talk()
  # 반갑습니다. 이학생입니다.
  # 저는 학생입니다.
  ```

<br>

## 캡슐화

- 객체의 일부 구현 내용에 대해 외부로부터의 직접적인 액세스를 차단
- 파이썬에서 기능상으로 존재하지 않지만, 관용적으로 사용되는 표현이 있음
- **접근제어자 종류**
  - `Public Access Modifier`
    - 언더바 없이 시작하는 메소드나 속성
    - 어디서나 호출이 가능, 하위 클래스 `override` 허용
  - `Protected Access Modifier`
    - **언더바 1개**로 시작하는 메소드나 속성
    - 암묵적 규칙에 의해부모 클래스 내부와 자식 클래스에서만 호출 가능
  - `Private Access Modifier`
    - **언더바 2개**로 시작하는 메소드나 속성
    - 본 클래스 내부에서만 사용이 가능