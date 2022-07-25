## 2번 두 개 뽑아서 더하기

```python
def solution(numbers):
    answer = set()
    for i in list(combinations(numbers,2)):
        answer.add(sum(i))
    return sorted(answer)

def solution(numbers):
    return sorted(list(set([sum([i,j]) for i,j in combinations(numbers,2)])))
```

`combinations()`

- 파이썬 기본 라이브러리인 itertools의 `combinations` 라는 내장함수를 사용하여 **인자값에 따라 해당 요소로 구할수 있는 모든 조합을 리턴한다.**
- ex) `combinations(numbers, 2)`는 numbers 리스트 안에 2개의 요소로 구할 수 있는 모든 조합을 반환

