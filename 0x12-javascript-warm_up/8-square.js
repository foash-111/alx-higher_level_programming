#!/usr/bin/node

const args = process.argv;
let i = 0;
let j = 0;
if (args[2] !== undefined){
  if (args[2] > 0){
      while (i < args[2]){
            console.log('X' * args[2]);
          i++;
      }
  }
  else{
      console.log('Missing size');
    }
      
}
else{
  console.log('Missing size');
}
