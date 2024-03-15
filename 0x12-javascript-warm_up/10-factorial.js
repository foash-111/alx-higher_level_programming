#!/usr/bin/node



/**
 * fact - return the factorial of any number passed to it
 * @param a 
 * @returns factorial of a
 */

function fact (a) {
  if (a <= 0) {
    return ('the factorial of negative numbers is undefined')
  }
  if (a === 1 || a === 0) {
    return (1);
  }
  return (a * fact(a - 1));
}

const args = process.argv;
let x = 1
let result = 1

if (isNaN(args[2]) === true) {
  console.log(x);
} else {
  x = parseInt(args[2]);
  console.log(fact(x));
}
