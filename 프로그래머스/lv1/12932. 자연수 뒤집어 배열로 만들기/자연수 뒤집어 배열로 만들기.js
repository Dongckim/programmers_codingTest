function solution(n) {
    let answer = []
    n.toString().split('').reverse().map((a)=>answer.push(+a))
    return answer
}