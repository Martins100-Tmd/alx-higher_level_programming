#!/usr/bin/node
const process = require('process');

let count = 0;
let i = 0;
while (process.argv[i] !== undefined) {
  count++;
  i++;
}
if (count === 2) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
