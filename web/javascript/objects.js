const rabbit = {
  name: 'rabbit'
};
// Methods are simply functions bound to an object
rabbit.speak = function() {
  console.log(this.name);
}

rabbit.speak();

// Arrow functions do not bind 'this' but regular functions do
rabbit.printName = function() { console.log(this.name) } // will print the rabbit's name
rabbit.printName = () => { console.log(this.name) } // undefined

// Every object has a prototype
console.log(Object.getPrototypeOf({}) == Object.prototype);

// Defining an object with class
class TestObject {
  constructor(y) {
    // By default accessing will check the constructor
    this.x = () => {console.log('in constructor')};
    this.y = y;
  }

  // methods are put in the prototype
  x() {
    console.log(`method: ${this.y}`);
  }
}

new TestObject('y').x(); // 'in constructor'
TestObject.prototype.x.call({y: 'hello'}); // 'method'
