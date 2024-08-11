#!/usr/bin/node

const request = require('request');

// Get the Movie ID from the command line arguments
const movieId = process.argv[2];

// Define the URL to fetch movie data
const movieUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Function to print character names
const printCharacterNames = (characterUrls) => {
    characterUrls.forEach((url) => {
        request.get(url, (err, response, body) => {
            if (err) {
                console.error(err);
                return;
            }
            const characterData = JSON.parse(body);
            console.log(characterData.name);
        });
    });
};

// Fetch the movie data
request.get(movieUrl, (err, response, body) => {
    if (err) {
        console.error(err);
        return;
    }
    const movieData = JSON.parse(body);
    const characterUrls = movieData.characters;
    printCharacterNames(characterUrls);
});
