## 암호문1

```python
명령어 = 명령어리스트[0]
if 명령어 == 'I'
    x = 명령어리스트[0+1]
    y = 명령어리스트[0+2]
    숫자_리스트=명령어리스트[0+3 : 0+3+y]

    for 숫자 in 숫자_리스트[::-1]
        암호문.insert(X, 숫자)
0 -> 1

T = 10
# ctrl + d
# 원본암호문 = [449047,855428,425117,532416,358612,929816,313459,311433,472478,589139,568205]

for t in range(1, T+1):
    origin_len = int(input())
    origin_list = list(map(int, input().split()))

    command_len = int(input())
    command_list = input().split()

    # i의 초기화
    i = 0
    
    # while문 (반복문)
    while i < len(command_list):
        command = command_list[i]
        if command == "I":
            # x,y,숫자리스트 s 구해야한다.
            x = int(command_list[i+1])
            y = int(command_list[i+2])
            # print(type(y))
            number_list = command_list[i+3 : i+3+y]

            # insert 메서드를 써서 x의 위치에 숫자들을 삽입한다.
            # 역순으로 삽입한다.
            for number in number_list[::-1]:
                origin_list.insert(x, int(number))

        # 0 + 1 -> 1
        i = i + 1
    

    # print(origin_list[:10])
    print(f"#{t}",*origin_list[:10])

```

- 파이썬 list의  메서드 `.insert(삽입위치, 값` 을 이용해 쉽게 풀 수 있다.
  - 값에는 숫자나 문자열이 들어가야함
- `*`를 하면 `unpacking`이 됨. 리스트나 튜플로 쌓여져 있던 값을 풀어줌
- while문 연습하기