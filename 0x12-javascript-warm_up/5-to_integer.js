#!/usr/bin/node

const args = process.argv;

if (args[2] !== undefined) {
  if (args[2] >= 0 ) {
    console.log('My number: ' + args[2]);
  } else {
    console.log('Not a number');
  }
} else {
    console.log('Not a number');
}
