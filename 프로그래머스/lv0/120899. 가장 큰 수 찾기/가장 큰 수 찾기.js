function solution(array) {
    return [Math.max(...array),array.findIndex(x=> x == Math.max(...array))]
}