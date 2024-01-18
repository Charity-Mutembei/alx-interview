#!/usr/bin/node
const request = require('request');
//declare the api link here
const myInteger = parseInt(process.argv[2], 10);

if (isNaN(myInteger)){
  //check if integer
  // console.error('Please input an integer in the command line argument');
  console.log('myInteger:', myInteger);
  process.exit(1);
  //meaning not a sucsess
}

//Append the integer taken into the URL argument
// const urlWithQuery = `${apiUrl}?myInteger=${myInteger}`;
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${myInteger}`;

//then make the request
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Request error:', error);
    return;
  }

  // Check if the request was successful (status code 200-299)
  if (response.statusCode < 200 || response.statusCode >= 300) {
    console.error(`HTTP error! Status: ${response.statusCode}`);
    return;
  }

  // Parse the JSON response
  const data = JSON.parse(body);

  // Handle the data from the API
  console.log(data);
});
