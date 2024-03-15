#!/usr/bin/node

const args = process.argv;

if (args[2] !== undefined) {
  if (args[3] !== undefined){
    console.log(args[2] + ' is ' + args[3])
  } else {
    console.log(args[2] + ' is undefined')
  }
} else {
  /* console.log(args[0]);
  console.log(args[1]); */
  console.log('undefined is undefined');
}
