#!/usr/bin/node
// convert the first int to int,when posible
// If the argument can’t be converted to an integer,
// print “Not a number”
const num = Math.floor(Number(process.argv[2]));
console.log(isNaN(num) ? 'Not a number' : `My number: ${num}`);
