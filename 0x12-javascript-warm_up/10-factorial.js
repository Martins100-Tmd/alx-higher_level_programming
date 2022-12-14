#!/usr/bin/node
// write a script that computes and prints a factorial.
const process = require('process');
const num = Math.floor(parseInt(process.argv[2]));
function RecurseFac (b, start = 1) {
  if (!b || isNaN(b)) {
    console.log(1);
    return;
  }
  if (b === 1) {
    console.log(start);
    return 1;
  }
  start *= b;
  b--;
  return RecurseFac(b, start);
}
RecurseFac(num);
