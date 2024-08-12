#!/usr/bin/node
/**
 * A script that prints all characters of a Star Wars movie.
 * The Movie ID is provided as a positional argument.
 */
const request = require('request');

// Get the movie ID from the command line arguments
const movieId = process.argv[2];

// Validate that the movie ID is provided
if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <movie_id>');
  process.exit(1);
}

// Construct the URL for the specified movie
const filmURL = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Fetch movie data
request(filmURL, (err, res, body) => {
  if (err) {
    console.error('Error fetching film data:', err);
    process.exit(1);
  }

  let filmData;
  try {
    filmData = JSON.parse(body);
  } catch (e) {
    console.error('Error parsing film JSON:', e);
    process.exit(1);
  }

  const charactersURLList = filmData.characters;

  if (!charactersURLList || charactersURLList.length === 0) {
    console.log('No characters found for this movie.');
    return;
  }

  // Fetch each character data
  charactersURLList.forEach((characterURL) => {
    request(characterURL, (err, res, body) => {
      if (err) {
        console.error('Error fetching character data:', err);
        return;
      }

      let characterData;
      try {
        characterData = JSON.parse(body);
        console.log(characterData.name);
      } catch (e) {
        console.error('Error parsing character JSON:', e);
      }
    });
  });
});

