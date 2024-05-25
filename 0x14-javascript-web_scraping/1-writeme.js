#!/usr/bin/node

const fs = require('fs');
const args = process.argv;

const data = args[3];

fs.writeFile(args[2], data, (err) => {
  if (err) {
    console.log(err);
  }
});

// fs.readFile(args[2], 'utf-8', (err, data) => {
//     if (err) {
//         console.log(err);
//         return;
//     }
// fs.writeFile(args[2], data, (err) => {
//    if (err) {
//     console.log(err);
//     return;
//    }
// })
// })
