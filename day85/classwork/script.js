// 1
function accum(s) {
  let result = []

  for (let i = 0; i < s.length; i++) {
    let part = s[i].toUpperCase() + s[i].toLowerCase().repeat(i)
    result.push(part)
  }

  return result.join("-")
}


// 2
function isIsogram(str) {
  str = str.toLowerCase()
  for (let i = 0; i < str.length; i++) {
    for (let j = i + 1; j < str.length; j++) {
      if (str[i] === str[j]) {
        return false
      }
    }
  }
  return true
}

// 3
function XO(str) {
  str = str.toLowerCase()
  let xCount = 0, oCount = 0
  for (let char of str) {
    if (char === "x") xCount++
    if (char === "o") oCount++
  }

  return xCount === oCount
}

// 4
function findShort(s) {
  const words = s.split(" ")
  const lengths = words.map(word => word.length)
  return Math.min(...lengths)
}

// 5
function maskify(cc) {
  cc = String(cc)
  if (cc.length <= 4) return cc
  let last4 = cc.slice(-4)
  let masked = "#".repeat(cc.length - 4)
  return masked + last4
}
