// Array.reduce: aggregate an array into a single object
const DOG = 'DOG';
const CAT = 'CAT';

let pets = [
  {
    name: "Chester",
    type: DOG
  },
  {
    name: "Snowball",
    type: CAT
  },
  {
    name: "Brownie",
    type: DOG
  }
]

const results = pets.reduce((aggregate, currentValue) => {
  let collection = aggregate;

  const { name, type } = currentValue;
  if (collection[type]) collection[type].push(name);
  else collection[type] = [name];

  return collection;
}, {})

console.log(results); // { DOG: [ 'Chester', 'Brownie' ], CAT: [ 'Snowball' ] }

// Array Map: apply a function to every item in an array and returns a new array
const mappedArray = [1, 2, 3, 4].map((el, index) => console.log(`${el}: ${index}`));

// Array Filter: filters an array based on a boolean condition
const filteredArray = [3, 2, 6, 7, 9, 8].filter(el => el > 5);




