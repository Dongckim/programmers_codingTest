function solution(left, right) {
    let answer = 0
    for(let j = left; j<=right; j++){
        answer += isPrimeNumber(j)
    }
    return answer
}

function isPrimeNumber(arg){
    const primeNumList = []
    for(let i = 1; i <= arg; i++){
        if(arg % i == 0){
            primeNumList.push(i)
        }
    }
    if((primeNumList.length) % 2==0){
        return +primeNumList[primeNumList.length - 1]
    }else{
        return -(+primeNumList[primeNumList.length - 1])
    }
}