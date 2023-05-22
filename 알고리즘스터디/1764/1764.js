const input = require('fs').readFileSync('/dev/stdin').toString().split('\n');

function solution1(input){
    const NohearSeen = new Set();
    input.map(item => NohearSeen.add(item))

    let DeleteElement = Array.from(NohearSeen).filter((item,index) => item !== input[index])
    let NohearSeenElement = input.filter((item,index) => item !== Array.from(NohearSeen)[index]).filter(item => !DeleteElement.includes(item))

    return [NohearSeenElement.length, ...NohearSeenElement]
}

function solution2(input){
    const [NoHear, NoSeen] = input[0].split(' ')
    let NoHearLst = input.slice(1, +NoHear+1)
    let NoSeenLst = input.slice(NoSeen)

    let answer = NoHearLst.filter(item => {
        for(let data in NoSeenLst){
            if(data == item){
                return true
            }
            else{
                return false
            }
        }
    })
    return answer
}

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

console.log(solution2(input))