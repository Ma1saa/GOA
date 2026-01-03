// 1 link: https://www.codewars.com/kata/5a2e9ae2b6cfd7692a0000ba/train/javascript

function typeOfSum(a, b) {
  return typeof (a + b);
}

// 2 link: https://www.codewars.com/kata/5a023c426975981341000014/train/javascript

function otherAngle(a, b) {
  return 180 - a - b
}

// 3 link: https://www.codewars.com/kata/51c8991dee245d7ddf00000e/train/javascript

function reverseWords(str){
  return str.split(" ").reverse().join(" ")
}

// 4 link: https://www.codewars.com/kata/56a4addbfd4a55694100001f/train/javascript

function validateHello(greetings) {
  greetings = greetings.toLowerCase();
  return greetings.includes("hello")
      || greetings.includes("ciao")
      || greetings.includes("salut")
      || greetings.includes("hallo")
      || greetings.includes("hola")
      || greetings.includes("ahoj")
      || greetings.includes("czesc");
}