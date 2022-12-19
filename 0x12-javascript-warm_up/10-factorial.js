#!/usr/bin/node
// Print the factorial of an argument recursively
function factorial (x) {
    if (x > 1) {
      return x * factorial(x - 1);
    } else {
    return 1;
  }
}
  const n = parseInt(process.argv[2]);
  console.log(factorial(n));