// Special Numbers
const inf = Infinity;
const negativeInf = -Infinity;
const nan = NaN;

// Strings
const singleQuoteString = 'this is a string';
const doubleQuoteString = "this is a string";
const backTickString = `This is a string ${singleQuoteString}`;


// Strings cannot be divided, multiplied or subtracted, but the + operator concates strings
const concatenatedString = 'This is a dog, ' + 'This is a cat';

// Unary operators

console.log(typeof 4.5) // Number
console.log(typeof "hello") // string


// Boolean
// use >, <, <==, >==, ===

// comparing strings. lowercase > uppercase; z > a; follows unicode standard
console.log("Z" < "a") // true
console.log("z" > "a") // true

// There is only one value in javascript that is not equal to itself
console.log(NaN === NaN) // false

// Logical Operators

// and &&
console.log(true && true);

// or ||
console.log(false || false);

// not !
console.log(!false);

// Empty values: null and undefined

// Short circuiting - only evaluate an expression until it satisfies the condition