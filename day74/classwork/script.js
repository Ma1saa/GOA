let clock = document.getElementById('count')
let time = 10
const btn = document.getElementById('btn')

btn.addEventListener('click', () => {
    let myTimer = setInterval(countdown, 1000)
    time = 10

})

function countdown () {
    if (time <= 0){
      clearInterval(myTimer)
  }else{
        time--
        clock.textContent = time
    }
}
