function solution(str) {
    let regex = /[^0-9]/g
    lengthCase = [4,6]
    return lengthCase.includes(str.length) ? !regex.test(str) : false
}