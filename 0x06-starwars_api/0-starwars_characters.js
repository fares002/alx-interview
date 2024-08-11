#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const baseUrl = 'https://swapi-api.alx-tools.com/api';

function fetchCharacter(url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(JSON.parse(body).name);
      }
    });
  });
}

async function getAndPrintCharacters() {
  try {
    const movieUrl = `${baseUrl}/films/${movieId}/`;
    const movieData = await new Promise((resolve, reject) => {
      request(movieUrl, (error, response, body) => {
        if (error) {
          reject(error);
        } else {
          resolve(JSON.parse(body));
        }
      });
    });

    const characterPromises = movieData.characters.map(fetchCharacter);
    const characters = await Promise.all(characterPromises);

    characters.forEach(character => console.log(character));
  } catch (error) {
    console.error('An error occurred:', error);
  }
}

getAndPrintCharacters();
