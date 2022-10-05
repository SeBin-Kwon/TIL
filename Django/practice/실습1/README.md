# django 실습 풀이

> 가상환경 파일은 꼭 .gitignore 파일로 제외시키기

```python
beer_list = [
 {'name' : '에델바이스', 'src':''},
]
```

```html
{{beer.name}}
{{beer.src}}
```

<br>

```python
lotto_list = []

# 딕셔너리를 잘 활용하는 것이 관건
lotto_result_list = [
  {'lotto' : [1,2,3,4,5], 'result':'1등-10억'},
  {'lotto' : [1,2,3,4,5], 'result':'1등-10억'},
  {'lotto' : [1,2,3,4,5], 'result':'1등-10억'},
  {'lotto' : [1,2,3,4,5], 'result':'1등-10억'},
  {'lotto' : [1,2,3,4,5], 'result':'1등-10억'},
]

for i in range(5):
  lotto = random.sample(range(1,46),6)
  lotto_list.append(lotto)

```

```html
{% for lotto in lotto_list %}
  {% for number in lotto %}
    <span>{{ number }}</span>
  {% endfor %}
  <br>
{% endfor %}
```

> url에서는 `_` (언더바)를 사용하지 않는다 `-` (하이픈)을 사용한다.