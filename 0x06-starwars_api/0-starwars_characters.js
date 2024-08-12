#!/usr/bin/node
const request = require('request');

// Get the movie ID from the command line arguments
const movieId = process.argv[2];

// Construct the URL for the specified movie
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Fetch movie data
request(url, (err, response, body) => {
    if (err) {
        console.error(err);
        return;
    }

    const movieData = JSON.parse(body);
    const characters = movieData.characters;

    // Function to fetch a single character's data and return a promise
    const fetchCharacter = (characterUrl) => {
        return new Promise((resolve, reject) => {
            request(characterUrl, (err, response, body) => {
                if (err) {
                    reject(err);
                } else {
                    const characterData = JSON.parse(body);
                    resolve(characterData.name);
                }
            });
        });
    };

    // Fetch all characters and print their names
    Promise.all(characters.map(fetchCharacter))
        .then(characterNames => {
            characterNames.forEach(name => console.log(name));
        })
        .catch(err => console.error(err));
});

