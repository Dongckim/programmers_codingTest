// 춘향이는 편의점 카운터에서 일한다.

// 손님이 2원짜리와 5원짜리로만 거스름돈을 달라고 한다. 
// 2원짜리 동전과 5원짜리 동전은 무한정 많이 가지고 있다. 
// 동전의 개수가 최소가 되도록 거슬러 주어야 한다. 
// 거스름돈이 n인 경우, 최소 동전의 개수가 몇 개인지 알려주는 프로그램을 작성하시오.

// 예를 들어, 거스름돈이 15원이면 5원짜리 3개를,

// 거스름돈이 14원이면 5원짜리 2개와 2원짜리 2개로 총 4개를, 
// 거스름돈이 13원이면 5원짜리 1개와 2원짜리 4개로 총 5개를 주어야 동전의 개수가 최소가 된다.

const input = require('fs').readFileSync('input.txt').toString().split('\n')[0];

function solution1(input){
    if(input === 3 || input === 1){
        return -1
    }
    let Acount = Math.floor(input/5)
    let remainder = input % 5
    if(remainder % 2 === 1){
        Acount--;
        remainder += 5 
    }
    return Acount + remainder/2
}

console.log(solution1(+input))