#!/usr/bin/node
// write a function that increments and call
// a function

exports.addMeMaybe = function (x, callback) {
  x = x + 1;
  callback(x);
};
