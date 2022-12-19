#!/usr/bin/node
// a script that prints a square
// argument is the size of the square
// if arg cannot be converted to int, print "Missing size"
const x = Math.floor(Number(process.argv[2]));
if (isNaN(x)) {
  console.log('Missing size');
} else {
  for (let r = 0; r < x; r++) {
    let row = '';
    for (let c = 0; c < x; c++) row += 'X';
    console.log(row);
  }
}
