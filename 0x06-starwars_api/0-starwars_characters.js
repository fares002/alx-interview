#!/usr/bin/node
/**
 * A script that prints all characters of a Star Wars movie.
 * The Movie ID is provided as a positional argument.
 */
const request = require('request');
const filmId = process.argv[2];  // Movie ID from command line argument
const filmURL = `https://swapi-api.alx-tools.com/api/films/${filmId}/`;  // URL to fetch film data

// Fetch film data
request(filmURL, async (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }
  try {
    const charactersURLList = JSON.parse(body).characters;  // Get characters URLs
    for (const characterURL of charactersURLList) {
      await new Promise((resolve, reject) => {
        // Fetch each character data
        request(characterURL, (err, res, body) => {
          if (err) {
            console.error(err);
            reject(err);
            return;
          }
          console.log(JSON.parse(body).name);  // Print character name
          resolve();
        });
      });
    }
  } catch (e) {
    console.error('Failed to parse JSON:', e);
  }
});

