function solution(x) {
    let harshad = String(x).split('')
    let sum = harshad.reduce((acc,curr)=> acc + +curr,0)
    return x%sum == 0
}