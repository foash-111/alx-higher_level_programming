#!/usr/bin/node

const args = process.argv;

if (args[2] !== undefined) {
  if (isNaN(args[2]) === false) {
    console.log('My number: ' + (args[2] | 0)); // Math.floor(args[2])
  } else {
    console.log('Not a number');
  }
} else {
  console.log('Not a number');
}
