const joinBtn = document.querySelector('#joinBtn')
joinBtn.addEventListener('click', function(event) {
  const password = document.querySelector('#password')
  console.log(event.target.value.length)
  if (password.value.length < 8) {
    alert('비밀번호는 8자리 이상으로 만들어주세요.');
  }
  const passwordCheck = document.querySelector('#password_confirmation')
  if (password.value !== passwordCheck.value) {
    alert('같은 비밀번호를 입력해주세요.');
  }
})