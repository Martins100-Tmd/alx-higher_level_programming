#!/usr/bin/node
//Write a script that reads and prints the content of a file
const fs = require('fs')
const process = require('process')
const file = process.argv[2]
fs.readFile(file, 'utf8', (err, data)=>{
	if(err)console.log(err)
	console.log(data);
})
