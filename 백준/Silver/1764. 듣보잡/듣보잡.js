const input = require('fs').readFileSync('/dev/stdin').toString().split('\n');
function solution3(input){
    const [NoHear, NoSeen] = input[0].split(' ')
    const HearSet = new Set();
    const SeenSet = new Set();
    for(let i = 1; i < input.length; i++){
        if(i < +NoHear+1){
            HearSet.add(input[i])
        }
        else{
            SeenSet.add(input[i])
        }
    }
    let answer = []
    Array.from(HearSet).map(item => SeenSet.has(item) ? answer.push(item) : null)
    return answer.length + '\n' +  answer.sort().join('\n')
}
console.log(solution3(input))