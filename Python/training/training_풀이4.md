# 실습 문제 풀이 4

## 문제 19 숫자의 길이 구하기

```python
number = 123

# 1. 문자열로 형변환
print(len(str(number)))

# 2. 123
cnt = 0
# 몫이 0이 되면 종료해야하니까
while number != 0:
# int : 0이 아닌 다른 수면 무조건 True
# while number: # 0이 되면 False라서 종료됨
    number //= 10
    cnt += 1
    
# 3. log
import math
print(int(math.log(number, 10)) + 1)
```

> 123 == 100 + 20 + 3 == 1 \* 100 + 2 \* 10 + 3 * 1

**while**

> 종료 조건 : 몫이 0

- 123 / 10 

  - 몫 => 12, 1, 0

  - 나머지 => 3, 2, 1