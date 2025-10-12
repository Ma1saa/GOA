const img = document.getElementById('img');
const btn1 = document.getElementById('btn1');
const btn2 = document.getElementById('btn2');
const btn3 = document.getElementById('btn3');


btn1.addEventListener('click', () => img.src = 'Untitled.jpg');
btn2.addEventListener('click', () => img.src = 'Untitled2.jpg');
btn3.addEventListener('click', () => img.classList = 'img1');
