const path = process.platform === 'linux' ? "/dev/stdin" : "input.txt";
const [num, mLoss] = require('fs').readFileSync(path).toString().split('\n');

fun