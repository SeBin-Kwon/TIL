# 🗺 이차원 리스트

> 이차원 리스트는 **행렬(matrix)** 이다.
>
> 이차원 리스트는 **리스트를 원소로 가지는 리스트** 이다.
>
> 보기 좋게 변경하면 행렬(matrix)의 형태가 나온다.

```python
matrix = [[1,2,3],[4,5,6],[7,8,9]]

print(matrix[0][0])
# 1
print(matrix[1][2])
# 6
print(matrix[2][1])
# 8
```

|       | 0    | 1    | 2    |
| ----- | ---- | ---- | ---- |
| **0** | 1    | 2    | 3    |
| **1** | 4    | 5    | 6    |
| **2** | 7    | 8    | 9    |

<br>

### 특정 값으로 초기화 된 이차원 리스트 만들기

1. **직접 작성** (4 x 3 행렬)

2. **반복문으로 작성** (100 X 100 행렬)

   ```python
   matrix = []
   for _ in range(100):
       matirix.append([0]*100)
   ```

   (n X m 행렬)

   ```python
   n = 4 # 행
   m = 3 # 열
   matrix = []
   
   for _ in range(n):
       matrix.append([0]*m)
       
   print(matrix)
   # [[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
   ```

   > n X m은 길이가 아닌 개수임

3. **리스트 컴프리헨션으로 작성** (n X m 행렬)

   ```python
   from pprint import pprint
   
   n = 10
   m = 10
   
   matrix = [[0]*m for _ in range(n)]
   
   print(matrix)
   ```

   > 값은 꼭 있어야함, None도 가능

<br>

### 🚨주의) 리스트 컴프리헨션 vs 리스트 곱셈 연산

> 리스트 곱셈 연산은 **메모리 주소값이 다 같게 설정되어 버린다.**

```python
n = 4 # 행
m = 3 # 열

matrix1 = [[0]*m for _ in range(n)]
matrix2 = [[0]*m]*n

matrix1[0][0] = 1
matrix2[0][0] = 1

print(matrix1)
# [[1,0,0], [0,0,0], [0,0,0], [0,0,0]]

print(matrix2)
# [[1,0,0], [1,0,0], [1,0,0], [1,0,0]]
```

<br>

## 입력 받기

### 행렬의 크기가 미리 주어지는 경우

1. **일단 초기화 하고 입력 읽고 바꾸기**
   - 8 X 8 [0]을 쭉 만들기
   
   - 입력 읽으면서 만약 F라면 1로 바꾸기
   
2. **입력을 그대로 이차원 리스트로 만들기**
   - `input 함수`가 한 줄을 입력 받기 때문에 **열의 크기는 사용 되지 않는다.**

```python
matrix = []

for _ in range(8):
    line = list(input())
    matrix.append(line)
    
# 리스트 컴프리헨션
matrix = [list(input()) for _ in range(8)]
```

- `split`은 공백이 있을 때 사용.
  - 다 이어진 str은 list로 형변환 했을 때 chr마다 원소로 넣어지므로 굳이 `split`할 필요 없다.

```python
matrix = []
for i in range(3):
    line = list(map(int,input().split()))
    matrix.append(line)
    
matrix = [list(map(int,input().split())) for i in range(3)]

# 8 7
matrix = [list(map(int,input().split())) for _ in range(n)]
```