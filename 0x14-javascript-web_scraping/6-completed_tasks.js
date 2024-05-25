#!/usr/bin/node

const request = require('request');

request(process.argv[2], (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const data = JSON.parse(body);
  // console.log(data);

  let i = 0;
  const info = {};
  let stringUserId = '';
  let count = 0;

  while (data[i] !== undefined) {
    if (data[i].completed === true) {
      count++;
      stringUserId = data[i].userId.toString();
      info[stringUserId] = count;

      if (data[i + 1].userId !== data[i].userId) {
        count = 0;
      }
    }
    i++;
  }

  console.log(info);
});
