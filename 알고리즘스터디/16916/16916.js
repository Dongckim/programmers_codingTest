const [s,p] = require('fs').readFileSync('input.txt').toString().split('\n');
console.log(s in p)