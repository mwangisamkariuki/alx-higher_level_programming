#!/usr/bin/node
class Rectangle {
    constructor (h, w) {
      if (( h > 0) && (w > 0)) {
        this.height = h;
        this.width = w;
      }
    }
  }
  
module.exports = Rectangle;
  