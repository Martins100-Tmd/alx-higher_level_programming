#!/usr/bin/node
// write a script that computes and prints a factorial.
const process = require('process');
const num = Math.floor(parseInt(process.argv[2]));
function RecurseFac (b, start = 1) {
  if (!b) return 1;
  if (b === 1) {
    console.log(start * num);
    return 1;
  }
  --b;
  start *= b;
  return RecurseFac(b, start);
}
RecurseFac(num);
