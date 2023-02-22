function solution(n) {
    let answer = []
    String(n).split('').sort().reverse().map((a)=>answer.push(+a))
    return +answer.join('')
}

function solution(n) {
    let answer = []
    let str = String(n).split('').sort().reverse()
    for(let i = 0; i < str.length; i++){
        answer.push(str[i])
    }
    return Number(answer.join(''))
}