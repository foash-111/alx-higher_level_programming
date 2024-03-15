#!/usr/bin/node

const args = process.argv;
let i = 0;
let j = 0;
if (args[2] !== undefined) {
  if (isNaN(args[2]) === false) {
      while (i < args[2] ){
          console.log('C is fun');
          i++;
      }
  } else {
      console.log('Missing number of occurrences');
    }
      
} else {
  console.log('Missing number of occurrences');
}
