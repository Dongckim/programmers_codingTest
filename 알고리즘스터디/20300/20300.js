const path = process.platform === 'linux' ? "/dev/stdin" : "input.txt";
const [num, mLoss] = require('fs').readFileSync(path).toString().split('\n');

function solution1(num, mLoss){
    mLoss = mLoss.split(' ').map(data => BigInt(data)).sort((a, b) => (a < b ? -1 : 1));
    // return mLoss.map(data => String(data))
    let answer = 0
    if(num % 2 === 0){
        for(let i = 0; i < num-1; i++){
            let sum = mLoss[i]+mLoss[num-(i+1)]
            answer = answer > sum ? answer :  sum
        }
        return String(answer)
    }
    else{
        answer = mLoss[num-1]
        for(let i = 0; i < num-2; i++){
            let sum = mLoss[i]+mLoss[num-(i+2)]
            answer = answer > sum ? answer :  sum
        }
        return String(answer)
    }
}

console.log(solution1(num, mLoss))

// 1 6 7 8 20 21 
// 10
// 1 9
// 2 5
// 3 4
