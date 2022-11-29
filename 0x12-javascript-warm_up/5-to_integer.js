#!/usr/bin/node
const process = require('process');
const num = Math.floor(parseInt(process.argv[2]));
num ? console.log(`My number: ${num}`) : console.log('Not a number');
