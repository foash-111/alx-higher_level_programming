#!/usr/bin/node

const request = require('request');

request(process.argv[2], (err, response, body) => {
    if (err) {
        console.error(err);
        return;
    }
    const data = JSON.parse(body)
    //console.log(data);
    // console.log(data.results[0].characters)
    // request(data.results[0].characters[0], (err, response, body) => {
    //     if (err) {
    //         console.log(err);
    //         return;
    //     }
    //     actor_info = JSON.parse(body)
    //     console.log(actor_info.name)
    //})

    let i = 0;
    let counter = 0;

    while(data.results[i] !== undefined) {
        let j = 0;
        while(data.results[i].characters[j] !== undefined) {

            actor_info_api = data.results[i].characters[j]
            Wedge_id = '18/'

            if (actor_info_api.slice(-3) === Wedge_id)
                {
                    counter++;
                }


            // request(data.results[i].characters[j], (err, response, body) => {
            //     if (err) {
            //         console.error(err);
            //         return;
            //     }
            //     actor_info = JSON.parse(body);
            //     if (actor_info.name === 'Wedge Antilles')
            //         {
            //             counter += 1;

            //         }

            // })

            j = j + 1
        }

        i = i + 1;
    }
    console.log(counter);
    })
