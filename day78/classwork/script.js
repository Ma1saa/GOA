// 1 link: https://www.codewars.com/kata/55eca815d0d20962e1000106/train/javascript
function generateRange(min, max, step){
    const range = [];
    for(let i = min; i <= max; i += step){
        range.push(i);
    }
    return range;
}

// 2 link: https://www.codewars.com/kata/55ecd718f46fba02e5000029/train/javascript
function between(a, b) {
  let betwin = []
  for(a; a<=b;a++){
    betwin.push(a)
  }
  return betwin
}

// 3 link: https://www.codewars.com/kata/583710ccaa6717322c000105/train/javascript
function simpleMultiplication(x) {
  if (x % 2 === 0) {
    return x * 8;
  } else {
    return x * 9;
  }
}

// 5 link: https://www.codewars.com/kata/5583090cbe83f4fd8c000051/train/javascript
function digitize(n) {
  n = String(n);
  let nm = [];
  for (let i = n.length - 1; i >= 0; i--) {
    nm.push(Number(n[i]));
  }
  return nm;
}