#!/usr/bin/node

// $.ajax({
//   url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
//   success: function (response) {
//     const body = JSON.parse(response);
//     $('#character').text(body.name);
//   }
// });

    $.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function(data) {
        
        $('#character').text(data.name);
    });


// request('https://swapi-api.alx-tools.com/api/people/5/?format=json', function(err, response, data) {
//     if (err) {
//         console.log(err);
//         return;
//     }
//     body = JSON.parse(data);
//     console.log(body);
//     $(document).ready('#character').text(body.name);
// })
