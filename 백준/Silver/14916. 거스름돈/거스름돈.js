const input = require('fs').readFileSync('/dev/stdin').toString().split('\n')[0];

function solution1(input){
    if(input === 3 || input === 1){
        return -1
    }
    let Acount = Math.floor(input/5)
    let remainder = input % 5
    if(remainder % 2 === 1){
        Acount--;
        remainder += 5 
    }
    return Acount + remainder/2
}

console.log(solution1(+input))