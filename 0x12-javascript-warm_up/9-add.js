#!/usr/bin/node
// Write a script that prints the addition of 2 integers
const process = require('process');
const num1 = Math.floor(parseInt(process.argv[2]));
const num2 = Math.floor(parseInt(process.argv[3]));

function add (a, b) {
  if (!a || !b) {
    console.log(NaN);
  } else {
    console.log(a + b);
  }
}
add(num1, num2);
