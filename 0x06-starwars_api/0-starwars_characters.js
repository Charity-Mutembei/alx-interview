#!/usr/bin/node

const request = require('request');

const myInteger = parseInt(process.argv[2], 10);

if (isNaN(myInteger)) {
  console.log('Please input an integer in the command line argument');
  process.exit(1);
}

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${myInteger}`;

function requestPromise (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(JSON.parse(body));
      }
    });
  });
}

async function main () {
  try {
    const filmData = await requestPromise(apiUrl);
    const characterLinks = filmData.characters;

    const charactersData = [];

    for (let i = 0; i < characterLinks.length; i++) {
      const characterData = await requestPromise(characterLinks[i]);
      charactersData.push({ index: i, name: characterData.name });
    }

    // Sort characters based on their original order in the API
    charactersData.sort((a, b) => a.index - b.index);

    // Print the sorted character names
    charactersData.forEach((character, index) => {
      console.log(`${character.name}`);
    });

    // console.log('All characters processed.');
  } catch (error) {
    console.error('Error:', error);
  }
}

main();
