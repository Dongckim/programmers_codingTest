function solution(arr, divisor) {
    let answer = []
    for(num of arr){
        num % divisor == 0 ? answer.push(num) : null
    }
    
    return answer == "" ? [-1] : answer.sort((a,b)=>a-b)
}