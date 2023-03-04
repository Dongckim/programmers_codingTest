function solution(numer1, denom1, numer2, denom2) {
    let LCM = 1
    while(true){
        if((LCM % denom1 == 0) && (LCM % denom2 == 0)){
            break;
        }
        LCM++;
    }
    let ans1 = numer1*(LCM/denom1) + numer2*(LCM/denom2)
    let GCD= 1
    for(let i =2; i<=Math.min(ans1,LCM); i++){
        if(ans1 % i === 0 && LCM % i === 0){
            GCD = i
        }
    }
    return [ans1/GCD, LCM/GCD]
}