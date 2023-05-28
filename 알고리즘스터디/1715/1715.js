const path = process.platform === 'linux' ? "/dev/stdin" : "input.txt";
const [num, ...input] = require('fs').readFileSync(path).toString().split('\n');

function solution1(num, input){
    let answer = 0
    do{
        input = input.map(data => +data).sort();
        input.push(input[0]+input[1])
        answer += input[input.length-1]
        input.shift();
        input.shift();
    }while(input.length > 1)

    return answer
}

function solution2(num, input){


}

console.log(solution1(num, input))