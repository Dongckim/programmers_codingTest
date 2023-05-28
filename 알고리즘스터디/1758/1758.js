const path = process.platform === 'linux' ? "/dev/stdin" : "input.txt";
const [num, ...input] = require('fs').readFileSync(path).toString().split('\n');

function solution1(num, input){
    const tips = input.join(',').trim().split(',').map(tip => +tip).sort((a,b) => b-a)
    let totalTips = 0
    for(let i = 1; i <= num; i++){
        let tipPerson = tips[i-1]-(i-1)
        if(Math.sign(tipPerson) === 1){
            totalTips += tipPerson;
        }else{
            tipPerson = 0;
        }
    }
    return totalTips
}

console.log(solution1(num, input))