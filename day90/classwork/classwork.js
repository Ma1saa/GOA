// 1 link:https://www.codewars.com/kata/59126992f9f87fd31600009b/train/javascript
function whoseMove(lastPlayer, win) {
  if(lastPlayer === "white"){
    if(win === true){
      return "white"
    }else{
      return "black"
    }
  }else{
    if(win === true){
      return "black"
    }else{
      return "white"
    }
  }
}

// 2 link:https://www.codewars.com/kata/57a77726bb9944d000000b06/train/javascript
function mango(quantity, price) {
  let total = 0;

  for (let i = 1; i <= quantity; i++) {
    if (i % 3 !== 0) {
      total += price;
    }
  }

  return total;
}

// 3 link:https://www.codewars.com/kata/59fc72fe235f93838b002235/train/javascript
function power(x,y){
  return x**y
}