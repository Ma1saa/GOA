const input = document.getElementById('celsius');
const result = document.getElementById('result');

function convert() {
    const celsius = input.value;
    const fahrenheit = celsius * 9 / 5 + 32;
    result.textContent = fahrenheit;
}