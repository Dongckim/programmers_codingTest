function solution(numbers) {
    let sums = []
    for(let i = 0; i < numbers.length-1; i++)
        for(let j = i+1; j < numbers.length;j++){
            let sum = numbers[i]+numbers[j]
            !sums.includes(sum) ? sums.push(sum) : null
        }
    return sums.sort((a,b)=> a-b)
}
/* let splicedNumber = numbers.splice(1,numbers.length-1)
    for(let i = 0; i < splicedNumber.length; i++){
            answer.push(numbers[0]+splicedNumber[i])
        }
    if(numbers.length == 1){
        return answer.sort((a,b)=>a-b).filter((n,idx) => idx == answer.indexOf(n));
    }
    else{
        solution(splicedNumber)
    }
    }*/