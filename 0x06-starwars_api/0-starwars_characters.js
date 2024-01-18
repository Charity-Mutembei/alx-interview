#!/usr/bin/node

const request = require('request');

const myInteger = parseInt(process.argv[2], 10);

if (isNaN(myInteger)) {
  console.log('Please input an integer in the command line argument');
  process.exit(1);
}

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${myInteger}`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Request error:', error);
    return;
  }

  if (response.statusCode < 200 || response.statusCode >= 300) {
    console.error(`HTTP error! Status: ${response.statusCode}`);
    return;
  }

  const data = JSON.parse(body);
  const characterLinks = data.characters;

  characterLinks.forEach(link => {
    requestAndPrintCharacter(link);
  });
});

function requestAndPrintCharacter (characterUrl) {
  request(characterUrl, (error, response, body) => {
    if (error) {
      console.error('Request error:', error);
      return;
    }

    if (response.statusCode < 200 || response.statusCode >= 300) {
      console.error(`HTTP error! Status: ${response.statusCode}`);
      return;
    }

    const characterData = JSON.parse(body);
    console.log(characterData.name);
  });
}
