#!/usr/bin/node
// Print the factorial of an argument recursively
function factorial (x) {
    if (isNaN(n)) {
        return 1;
    }
    if (x > 1) {
      return x * factorial(x - 1);
    }
    if (x < 0) {
      return undefined;
    }
  }
  const n = parseInt(process.argv[2]);
  console.log(factorial(n));
