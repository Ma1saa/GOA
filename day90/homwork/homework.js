// 1 link:https://www.codewars.com/kata/53dbd5315a3c69eed20002dd/train/javascript
function filter_list(l) {
  return l.filter(e => {
    return Number.isInteger(e)
  })
}
// 2 link:https://www.codewars.com/kata/554b4ac871d6813a03000035/train/javascript
function highAndLow(numbers) {
  const nums = numbers.split(' ').map(Number)
  const max = Math.max(...nums)
  const min = Math.min(...nums)

  return `${max} ${min}`
}
// 3 link:https://www.codewars.com/kata/54ff3102c1bad923760001f3/train/javascript
function getCount(str) {
  const vowels = "aeiou"
  let count = 0
  for (let char of str) {
    if (vowels.includes(char)) {
      count++
    }
  }

  return count
}
// 4 link:https://www.codewars.com/kata/55908aad6620c066bc00002a/train/javascript
function XO(str) {
  str = str.toLowerCase()
  let xCount = 0, oCount = 0
  for (let char of str) {
    if (char === "x") xCount++
    if (char === "o") oCount++
  }

  return xCount === oCount
}