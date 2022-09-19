const previousBtn = document.querySelector('#previousBtn')
    previousBtn.addEventListener('click', function() {
      const currentElement = document.querySelector('.active')
      const items = document.querySelectorAll('.carousel-item')
      let idx = [...items].indexOf(currentElement)
      currentElement.classList.toggle('active')
      if (idx === 0){
        idx = 3
      } else {
        idx -= 1
      }
      items[idx].classList.toggle('active')
      console.log(currentElement, items, idx)
    })

// const previousBtn = document.querySelector('#previousBtn')
// previousBtn.addEventListener('click', function() {
//   const currentElement = document.querySelector('.active')
//   const items = document.querySelectorAll('.carousel-item')
//   const idx = [...items].indexOf(currentElement)
//   console.log(currentElement, items, idx)
//   currentElement.classList.toggle('active')
//   items[(items.length+idx-1)%items.length].classList.toggle('active')
// })

const nextBtn = document.querySelector('#nextBtn')
    nextBtn.addEventListener('click', function() {
      // 지금 active인 것은 어떻게 알죠?
      const currentElement = document.querySelector('.active')
      // 전체 item 중에....... 이 Element의 인덱스?
      const items = document.querySelectorAll('.carousel-item')
      const idx = [...items].indexOf(currentElement)
      currentElement.classList.toggle('active')
      items[(idx+1)%items.length].classList.toggle('active')
      console.log(currentElement, items, idx)
    })


    // let cnt = 0
    // next_btn.addEventListener('click', function() {
    //     carousel_item[cnt%5].style.display = 'none';
    //     cnt += 1;
    //     carousel_item[cnt%5].style.display = 'block';
    // });
    
    // previous_btn.addEventListener('click', function() {
    //     carousel_item[cnt%5].style.display = 'none';
    //     cnt -= 1;
    //     if (cnt === -1) {
    //         cnt = 4
    //     }
    //     carousel_item[cnt%5].style.display = 'block';
    // });