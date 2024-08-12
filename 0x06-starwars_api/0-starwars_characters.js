#!/usr/bin/node

const request = require('request');

// Get the movie ID from command line arguments
const movieId = process.argv[2];

// Base URL for the Star Wars API
const baseUrl = 'https://swapi-api.alx-tools.com/api';

// Function to make a GET request and return a promise
function makeRequest(url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) reject(error);
      else resolve(JSON.parse(body));
    });
  });
}

// Main async function
async function getAndPrintCharacters() {
  try {
    // Get movie data
    const movieData = await makeRequest(`${baseUrl}/films/${movieId}/`);
    
    // Get and print character names
    for (const characterUrl of movieData.characters) {
      const characterData = await makeRequest(characterUrl);
      console.log(characterData.name);
    }
  } catch (error) {
    console.error('An error occurred:', error);
  }
}

// Run the main function
getAndPrintCharacters();
