# AJAX

> Asynchronous JavaScript And XML
>
> 요즘은 XML이 아닌 JSON을 사용

- 비동기식
  - 병렬적 Task 수행
  - 요청을 보낸 후 응답을 기다리지 않고 다음 동작이 이루어짐 (non-blocking)

### Event Loop 기반 동시성 모델

## Axios

- 브라우저를 위한 Promise 기반의 클라이언트

### 1. CDN 가져오기

- 사용자가 비동기 요청을 보내면 JSON으로 응답해줌
- 새로고침 없이도 화면 데이터가 바뀜
- 클라이언트 쪽에서 처리해서 서버 쪽에도 부담이 없음

- 좋아요 버튼 누르면 새로고침 되는 것이 아니라 그 자리에서 바로 색과 카운트를 바꿈
- 구글 맵에서 지도를 움직일 때, 바로바로 바깥쪽에 있던 영역을 붙여줌

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>

<body>
  <button>클릭</button>
  <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
  <script>
    const body = document.querySelector('body')
    const title = document.createElement('h1')
    title.innerText = 'AJAX'
    body.appendChild(title)

    const button = document.querySelector('button')
    // 버튼을 클릭하면, 함수를 실행해주ㅜ
    button.addEventListener('click', function () {
      const URL = 'https://jsonplaceholder.typicode.com/todos/1'
      // axios는 URL로 요청을 보내줌.
      // 처리가 완료되면 실행시켜주겠다는 약속(promise)
      // 성공적이면 then, 실패면 catch
      axios.get(URL)
        .then(response => {
          // 성공해서 받은 응답 객체를 활용한 조작
          const h2 = document.createElement('h2')
          h2.innerText = response.data.title
          body.appendChild(h2)
          const p = document.createElement('p')
          p.innerText = response.data.userId
          body.appendChild(p)
        })
        .catch(err => console.log(`${err}!!!`))
    })
  </script>
</body>

</html>
```

- a태그가 필요 없게된다.
- url을 통해 views.py로 보내고 JSON응답을 리턴한다.
- 파이썬의 모델 객체를 사용할 수 없다 => 값을 보내야한다. => 불린값

