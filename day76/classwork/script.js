const input1 = document.getElementById('input1')
const input2 = document.getElementById('input2')
const input3 = document.getElementById('input3')
const input4 = document.getElementById('input4')
const btn = document.getElementById('btn')
const div = document.getElementById('div')
let divPosition = 0

let favFoods = [input1.value, input2.value, input3.value, input4.value]
console.log(favFoods)

btn.addEventListener('click', () => {
    divPosition += 50
    div.style.left = divPosition + 'px'
})