function exampleOne() {
  console.log('example one');
}

const exampleTwo = function() {
  console.log('example two');
}

const exampleThree = () => {
  console.log('example three');
}

/**
 * Closure
 * How local binding is treated when a function is declared within a function
 * local binding is created for each binding
 * Being able to reference a specific instance of a local binding in an enclosing scope is called closure
 */

function wrapValue(n) {
  let local = n;
  return () => local;
}

let wrap1 = wrapValue(1); // 1
let wrap2 = wrapValue(2); // 2


/**
 * Higer-ordered functions
 * Functions that operate on other functions, either by taking them as arguments or by returning them
 */