const inputText = document.querySelector('#input-text')

inputText.addEventListener('input', function(event) {
  const myText = document.querySelector('#my-text')
  myText.innerText = event.target.value
  // console.log(event.target.value)
})