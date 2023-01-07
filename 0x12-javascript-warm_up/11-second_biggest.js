#!/usr/bin/node
// write a script that search for the
// second largest integer in a list.
const process = require('process');
let array = process.argv.slice(2).map((item) => {
  return parseInt(item);
});
if (process.argv.length === 2) {
  console.log(0);
} else if (array.length === 1) {
  console.log(array[0]);
} else {
  array = array.sort((a, b) => {
    return a - b;
  });
  console.log(array[array.length - 2]);
}
