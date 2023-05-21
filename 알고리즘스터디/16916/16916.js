const input = require('fs').readFileSync('input.txt').toString().split('\n');

function solution1([p,s]){

    return p.split(s) === p[0] ? 0 : 1 
}

function solution2([p,s]){
    
}

console.log(solution1(input))