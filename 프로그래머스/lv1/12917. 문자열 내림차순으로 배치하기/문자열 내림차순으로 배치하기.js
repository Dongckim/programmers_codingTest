function solution(s) {
    const UpperCase = s.split('').filter(item=> item == item.toUpperCase()).sort().reverse()
    const LowerCase = s.split('').filter(item=> item == item.toLowerCase()).sort().reverse()
    return [...LowerCase, ...UpperCase].join('')
}