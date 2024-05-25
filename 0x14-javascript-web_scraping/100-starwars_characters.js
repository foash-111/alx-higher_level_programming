#!/usr/bin/node

const request = require('request');

request('https://swapi-api.alx-tools.com/api/films/', (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const data = JSON.parse(body);
  // console.log(data);

  let i = 0;

  while (data.results[i] !== undefined) {
    if (data.results[i].episode_id === parseInt(process.argv[2])) {
      let j = 0;
      while (data.results[i].characters[j] !== undefined) {
        request(data.results[i].characters[j], (err, response, body) => {
          if (err) {
            console.error(err);
            return;
          }
          const actorInfo = JSON.parse(body);
          console.log(actorInfo.name);
        });

        j = j + 1;
      }
      break;
    }

    i = i + 1;
  }
});
