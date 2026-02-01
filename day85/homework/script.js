// 1
function filter_list(l) {
  return l.filter(e => {
    return Number.isInteger(e)
  })
}

// 2
function highAndLow(numbers) {
  const nums = numbers.split(' ').map(Number)
  const max = Math.max(...nums)
  const min = Math.min(...nums)

  return `${max} ${min}`
}
// 3
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
// 4
function XO(str) {
  str = str.toLowerCase()
  let xCount = 0, oCount = 0
  for (let char of str) {
    if (char === "x") xCount++
    if (char === "o") oCount++
  }

  return xCount === oCount
}
// 5
function likes(names) {
  const count = names.length

  if (count === 0) {
    return "no one likes this"
  } else if (count === 1) {
    return `${names[0]} likes this`
  } else if (count === 2) {
    return `${names[0]} and ${names[1]} like this`
  } else if (count === 3) {
    return `${names[0]}, ${names[1]} and ${names[2]} like this`
  } else {
    return `${names[0]}, ${names[1]} and ${count - 2} others like this`
  }
}
