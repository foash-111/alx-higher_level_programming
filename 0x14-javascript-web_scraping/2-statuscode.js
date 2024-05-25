#!/usr/bin/node

// const fetch = require('node-fetch');

// To this
// import fetch from 'node-fetch';

// const args = process.argv;

// fetch(args[2])
//   .then(response => {
//     console.log(response.status);
//   })
//   .catch(err => console.log(err));
const request = require('request');

const args = process.argv;

request(args[2], (err, response) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log('code:', response.statusCode);
});
