function solution(arr){
    let answer = []
    
    arr.filter((word,index)=>{
        word != arr[index+1] ? answer.push(word) : null
    })
    return answer
}