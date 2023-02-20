function solution(arr) {
    return arr.length == 1 ? [-1] : arr.filter((element) => element !=Math.min(...arr))
}