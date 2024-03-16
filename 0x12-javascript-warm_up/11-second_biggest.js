#!/usr/bin/node

const args = process.argv;
let i = 2;
let current = 0
let big = 0;
let secBig = 0;


/*args[0], is the  filename, args[1] is the path to this file */
/**/
if (isNaN(args[3]) === true) {
  console.log('0');
} else {

  big = parseInt(args[i]);
  secBig = parseInt(args[i]);

  while (args[i] !== undefined)
  {
    current = parseInt(args[i]);

    if (current > big) {
      secBig = big;
      big = current;
    }
    else if (current > secBig) {
      secBig = current;
    }
    i++;
  }
  console.log(secBig);
 
}
