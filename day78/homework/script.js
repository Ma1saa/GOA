let strns = ['yes', 'no', 'maybe']

let strnss = strns.map(str => `!!! ${str}`)

console.log(strnss)

let names = ['ali', 'veli', 'serkan']

let names2 = names.map(name => `Dear ${name}`)

console.log(names2)

let numbers = [1, 2, 3, 4, 5]

let numbers2 = numbers.map(num => `${num} €`)

console.log(numbers2)

let strYears = ['2019', '2020', '2021']

let strYears2 = strYears.map(year => `Born in ${year}`)

console.log(strYears2)

let product = [{
    name: 'phone',
    price: 1000,
    discount: 20
}]

let discountedProduct = product.map(prod => `name: ${prod.name}, price: ${prod.price - prod.price * (prod.discount / 100)}`)


console.log(discountedProduct)

let words = ['hello', 'world', 'how', 'are', 'you']

let words2 = words.map(word => word.length <= 4 ?  word : "Too long!")

console.log(words2)

let numbers3 = numbers.map(num => `<<${num}>>`)

console.log(numbers3)

let bool = [true, false, true]

let bool2 = bool.map(bol => bol ? 'Yes' : 'No')

console.log(bool2)

const cities = ["Tbilisi", "Batumi", "Kutaisi"]

const options = cities.map(city => `<option>${city}</option>`)

console.log(options)

namess = [{
    firstName: 'mate',
    lastName: 'maisuradze',
}]

let names3 = namess.map(name => `${name.lastName.toUpperCase()}, ${name.firstName.toUpperCase()}`)

console.log(names3)

// 1 link: https://www.codewars.com/kata/5715eaedb436cf5606000381/train/javascript

function positiveSum(arr) {
  return arr.reduce((sum, num) => {
    return num > 0 ? sum + num : sum
  }, 0)
}

// 2 link: https://www.codewars.com/kata/57a2013acf1fa5bfc4000921/train/javascript

function findAverage(array) {
  if (array.length === 0) return 0
  let sum = array.reduce((acc, num) => acc + num, 0)
  return sum / array.length
}

// 3 link: https://www.codewars.com/kata/55d24f55d7dd296eb9000030/train/javascript

var summation = function (num) {
  let sum = 0
  for (let i = 1; i <= num; i++) {
    sum += i
  }
  return sum
}