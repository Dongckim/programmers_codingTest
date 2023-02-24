function solution(s){
    let answer = true;
    let lowerCase = s.toLowerCase()
    let countP = 0
    let countY = 0
    lowerCase.split('').map((element) => {
        if(element == 'p'){
            countP++
        }else if(element == 'y'){
            countY++
        }
    })
    return countP == countY
}   