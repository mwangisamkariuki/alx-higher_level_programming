#!/usr/bin/node
class Rectangle {
    constructor (h, w) {
      if (( h > 0) && (w > 0)) {
        this.width = w;
        this.height = h;
      }
    }
}

module.exports = Rectangle;
  