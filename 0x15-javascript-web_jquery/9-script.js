#!/usr/bin/node


$.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function(data) {

        $('#hello').html('<li>' + data.hello + '</li>');
    });

// const request = require('request')

// request('https://hellosalut.stefanbohacek.dev/?lang=fr', (err, response, data) => {
//     if (err) {
//         console.log(err);
//         return;
//     }
//     {
//         body = JSON.parse(data);
//         console.log(body)
//     }
// })
