let container = document.getElementById('container')

toggle = () => {
  container.classList.toggle('sign-in')
  container.classList.toggle('sign-up')
}

function toggle() {
  const container = document.getElementById("container");
  container.classList.toggle("active");
}


setTimeout(() => {
  container.classList.add('sign-in')
}, 200)