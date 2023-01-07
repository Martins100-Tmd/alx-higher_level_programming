#!/usr/bin/node
function change () {
  this.myVar = 333;
}
change();
module.exports = { change };
