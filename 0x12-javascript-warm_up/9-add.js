#!/usr/bin/node

const args = process.argv;

function add (a, b) {
  return (a + b);
}

if (isNaN(args[2]) === true || isNaN(args[3] === true)) {
  console.log('NaN');
} else {
  console.log(add(parseInt(args[2]), parseInt(args[3])));
}
