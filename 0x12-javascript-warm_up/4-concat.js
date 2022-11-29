#!/usr/bin/node
const process = require('process');
if (process.argv) {
  const a = process.argv[2];
  const b = process.argv[3];
  console.log(a + ' is ' + b);
}
