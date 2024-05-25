#!/usr/bin/node

const request = require('request');

request(process.argv[2], (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const data = JSON.parse(body);
  // console.log(data);
  // console.log(data.results[0].characters)
  // request(data.results[0].characters[0], (err, response, body) => {
  //     if (err) {
  //         console.log(err);
  //         return;
  //     }
  //     actor_info = JSON.parse(body)
  //     console.log(actor_info.name)
  // })

  let i = 0;
  let counter = 0;

  while (data.results[i] !== undefined) {
    let j = 0;
    while (data.results[i].characters[j] !== undefined) {
      const actorInfoApi = data.results[i].characters[j];
      const WedgeId = '18/';

      if (actorInfoApi.slice(-3) === WedgeId) {
        counter++;
      }

      j = j + 1;
    }

    i = i + 1;
  }
  console.log(counter);
});
