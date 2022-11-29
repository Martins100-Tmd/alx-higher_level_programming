#!/usr/bin/node
const process = require('process');
if (process.argv.length > 2) {
  const a =
    process.argv.length[2] !== null ? process.argv.length[2] : undefined;
  const b =
    process.argv.length[3] !== null ? process.argv.length[3] : undefined;
  console.log(a + ' is ' + b);
}
