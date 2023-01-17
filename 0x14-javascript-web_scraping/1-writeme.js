#!/usr/bin/node
// write a script tht wrties a string to a file
const fs = require('fs');
const process = require('process');
const file = process.argv[2];
const text = process.argv[3];
fs.writeFile(file, text, 'utf8', (err, data) => {
  if (err)console.log(err);
});
