#!/usr/bin/node

const args = process.argv;
let i = 0;
let j = 0;
if ((args[2] === undefined) || (isNaN(args[2]) === true)) {
  console.log('Missing number of occurrences');   
} else {
  while (i < args[2]) {
    console.log('C is fun');
    i++;
}
}
