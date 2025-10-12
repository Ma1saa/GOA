const btn = document.getElementById('btn');
const btn1 = document.getElementById('btn1');
const img = document.getElementById('img');
const btn2 = document.getElementById('btn2');

btn.addEventListener('click', () => {console.log('5')})

btn.removeEventListener('click', () => {console.log('5')})

btn1.addEventListener('pointerdown', () => {img.src = 'Untitled2.jpg'})

btn2.addEventListener('pointerup', () => {console.log('you lost')})
