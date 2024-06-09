#!/usr/bin/node


$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function(data) {
let i = 0;
while(data.results[i] !== undefined)
    {
        $('#list_movies').append('<li>' + data.results[i].title + '</li>');
        i++;
    }
    });

// const request = require('request')

// request('https://swapi-api.alx-tools.com/api/films/?format=json', (err, response, data) => {
//     if (err) {
//         console.log(err);
//         return;
//     }
//     {
//         body = JSON.parse(data);
//         console.log(body)
//     }
// })
