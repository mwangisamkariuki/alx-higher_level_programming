#!/usr/bin/node
const SquareII = require('./5-square');

class Square extends SquareII {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        let s = '';
        for (let j = 0; j < this.width; j++) {
          s += 'C';
        }
        console.log(s);
      }
    }
  }
}

module.exports = Square;
