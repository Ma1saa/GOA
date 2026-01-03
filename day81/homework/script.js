// 1 link:https://www.codewars.com/kata/5a6663e9fd56cb5ab800008b/train/javascript

var humanYearsCatYearsDogYears = function(humanYears) {
  let dog = 24
  let cat = 24
  let years = humanYears - 2
  if(humanYears == 1){
    return [1,15,15]
  }else if(humanYears == 2){
    return [2,24,24]
  }else{
    return[humanYears,cat+years*4,dog+years*5]
  }
}

// 2 link:https://www.codewars.com/kata/5ce9c1000bab0b001134f5af/train/javascript

const quarterOf = (month) => {
  if (month <= 3) return 1
  if (month <= 6) return 2
  if (month <= 9) return 3
  return 4
}

// 3 link:https://www.codewars.com/kata/526471539d52735c620000c6/train/javascript

function Counter() {
  this.value = 0
}

Counter.prototype.increase = function () {
  this.value++
}

Counter.prototype.getValue = function () {
  return this.value
}

Counter.prototype.reset = function () {
  this.value = 0
}

// 4 link:https://www.codewars.com/kata/54147087d5c2ebe4f1000805/train/javascript

function _if(bool, func1, func2) {
  return bool ? func1() : func2();
}

// 5 link:https://www.codewars.com/kata/57a1fd2ce298a731b20006a4/train/javascript

function isPalindrome(x) {
  return x.split("").reverse().join("").toLowerCase() == x.toLowerCase() ? true : false
}


