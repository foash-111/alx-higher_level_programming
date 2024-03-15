#!/usr/bin/node

const args = process.argv;
let i = 0;
let arr = '';
if ((args[2] === undefined) || (isNaN(args[2]) === true)) {
  console.log('Missing size');
} else {
  while (i < args[2]) {
    arr += 'X';
    i++;
  }
  i = 0;
  while (i < args[2]) {
    console.log(arr);
    i++;
  }
}
