#!/usr/bin/node
// Check if it is a number
// Print 'C is fun" times the argument passed
// Else print 'Missing number of occurences' if no argument
const x = Math.floor(Number(process.argv[2]));
if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
