#!/usr/bin/node
exports.logMe = function (item) {
  if (exports.logMe.numArgs === undefined) {
    numArgs = 0;
  }
  console.log(numArgs + ': ' + item);
  numArgs++;
};
