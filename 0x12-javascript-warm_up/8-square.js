#!/usr/bin/node
const process = require('process');
const num = Math.floor(parseInt(process.argv[2]));

if (process.argv[2]) {
  if (num > 0) {
    if (typeof num === 'number') {
      let sum = '';
      let i = 0;
      while (i < num) {
        sum += 'X';
        i++;
      }
      i = 0;
      while (i < num) {
	console.log(sum);
	i++;
      }
    }
  }
} else {
  console.log('Missing size');
}
