#!/usr/bin/node
// a script that prints a square
// argument is the size of the square
// if arg cannot be converted to int, print "Missing size"
const x = Math.floor(Number(process.argv[2]));
if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
    for (let row = 0; row < x; row++){
      let row = '';
      for (let column = 0; column < x; column++) row+='X';
      console.log(row)
    }
}
