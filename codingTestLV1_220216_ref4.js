/**
정수 배열 numbers가 주어집니다. 
numbers에서 서로 다른 인덱스에 있는 두 개의 수를 뽑아 더해서 만들 수 있는 모든 수를 배열에 오름차순으로 담아 return 하도록 solution 함수를 완성해주세요.



제한사항
numbers의 길이는 2 이상 100 이하입니다.
numbers의 모든 수는 0 이상 100 이하입니다.
*/


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