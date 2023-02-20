function solution(numbers) {
    let answer = []
    let intBox = [1,2,3,4,5,6,7,8,9]
    for(num of numbers){
        for(let int of intBox){
            numbers.join('').includes(int) ? null : answer.push(int)
        }
    }
    let uniqueNum = answer.filter((element,index) => answer.indexOf(element)==index)
    return uniqueNum.reduce((a,b)=>a+b)
}
