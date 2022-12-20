#!/usr/bin/node
const fs = require('fs');

const fArgs = fs.readFileSync(process.argv[2], 'utf8');
const sArgs = fs.readFileSync(process.argv[3], 'utf8');
fs.writeFileSync(process.argv[4], fArgs + sArgs);