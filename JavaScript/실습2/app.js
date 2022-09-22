const lottoBtn = document.querySelector('#btn')
lottoBtn.addEventListener('click', function() {
  const ballList = document.createElement('div')
  ballList.classList.add('ball-list')
  // 번호 랜덤 뽑기, 배열
  const number = _.sampleSize(_.range(1,46),6)
  console.log(number)
  // 반복시키기
  for (num of number) {
    const ball = document.createElement('div')
    ball.classList.add('ball')
    ball.innerText = num
    if (num < 11) {
      ball.style.backgroundColor = 'rgb(255, 191, 0)';
    } else if (num < 21) {
      ball.style.backgroundColor = 'rgb(53, 137, 254)';
    } else if (num < 31) {
      ball.style.backgroundColor = 'rgb(255, 82, 82)';
    } else if (num < 41) {
      ball.style.backgroundColor = 'rgb(166, 166, 166)';
    } else {
      ball.style.backgroundColor = 'rgb(72, 211, 93)';
    }
    ballList.appendChild(ball)
  }
  const result = document.querySelector('#result')
  result.appendChild(ballList)
})

const lottoCnt = document.querySelector('#cnt')
lottoCnt.addEventListener('click', function() {
  const cnt = prompt('개수를 지정해 주세요.', 1)
  for (let i = 0; i < cnt; i++) {
    const ballList = document.createElement('div')
    ballList.classList.add('ball-list')
    // 번호 랜덤 뽑기, 배열
    const number = _.sampleSize(_.range(1,46),6)
    console.log(number)
    // 반복시키기
    for (num of number) {
      const ball = document.createElement('div')
      ball.classList.add('ball')
      ball.innerText = num
      if (num < 11) {
        ball.style.backgroundColor = 'rgb(255, 191, 0)';
      } else if (num < 21) {
        ball.style.backgroundColor = 'rgb(53, 137, 254)';
      } else if (num < 31) {
        ball.style.backgroundColor = 'rgb(255, 82, 82)';
      } else if (num < 41) {
        ball.style.backgroundColor = 'rgb(166, 166, 166)';
      } else {
        ball.style.backgroundColor = 'rgb(72, 211, 93)';
      }
      ballList.appendChild(ball)
    }
    const result = document.querySelector('#result')
    result.appendChild(ballList)
  }  
})

