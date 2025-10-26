const p = document.getElementById("p")
const btn1 = document.getElementById("btn1")
const btn2 = document.getElementById("btn2")
const div = document.getElementById("box")
const btn3 = document.createElement("button")
const p1 = document.getElementById("p1")
const img = document.querySelector("img")
let myTimer
let count = 0
let bCount = 10

btn3.style.backgroundColor = "red"
btn3.textContent = "stop"


btn1.addEventListener("click", () => {
    myTimer = setInterval(stopWatch, 1000)
    div.replaceChild(btn3, btn1)
})

btn3.addEventListener('click', () => {
    div.replaceChild(btn1, btn3)
    clearInterval(myTimer)
})

btn2.addEventListener("click", () => {
    count = 0
    p.textContent = count
    clearInterval(myTimer)
    div.replaceChild(btn1, btn3)
})

function stopWatch(){
    console.log(count)
    p.textContent = count
    count++
}

function hello(){console.log("Hello World")}
setInterval(hello,1000)

function bombCountdown(){
    p1.textContent = bCount
    bCount--
    if (bCount < 0){
        clearInterval(bombTimer)
        img.src = 'Untitled1.jpg'
    }
}

let bombTimer = setInterval(bombCountdown, 1000)