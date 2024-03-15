#!/usr/bin/node

const args = process.argv;

if (args[2] !== undefined) {
  console.log('Arguments found');
} else {
  /* console.log(args[0]);
  console.log(args[1]); */
  console.log('No argument');
}
