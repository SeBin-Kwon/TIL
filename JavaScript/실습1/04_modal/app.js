const modalToggle = function(event) {
  document.querySelector('#modal-content').classList.toggle('active')
  event.stopPropagation()
}

const modalBtn = document.querySelector('#modal-btn')
modalBtn.addEventListener('click', modalToggle)

const modalCancel = document.querySelector('#modal-cancel')
modalCancel.addEventListener('click', modalToggle)

const modalCancelOverlay = document.querySelector('#modal-content')
modalCancelOverlay.addEventListener('click', modalToggle)

// const modalOverlay = document.querySelector('#modal-content')
// propagation