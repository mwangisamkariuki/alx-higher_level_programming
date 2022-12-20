#!/usr/bin/node
class Rectangle {
    constructor (h, w) {
      if ((w > 0) && (h > 0)) {
        this.width = w;
        this.height = h;
      }
    }
}

module.exports = Rectangle;
