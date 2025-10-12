const car = {
  brand: "Toyota",
  model: "Corolla",
  year: 2020,
  info: function() {
    return `This car is a ${this.year} ${this.brand} ${this.model}`;
  }
};
console.log(car.info());

const student = {
  name: "Giorgi",
  grades: {
    math: 90,
    english: 85,
    history: 95
  }
};
const values = Object.values(student.grades);
const average = values.reduce((a, b) => a + b, 0) / values.length;
console.log(`Average grade: ${average}`);

const book = {
  title: "Harry Potter",
  author: "J.K. Rowling"
};
document.body.innerHTML += `<h2>${book.title}</h2><p>Author: ${book.author}</p>`;
