function solution(absolutes, signs) {
    let sumBox = 0
    for(let i = 0; i < signs.length; i++){
        if(signs[i] === true){
            sumBox += absolutes[i]
        }else{
            sumBox -= absolutes[i]
        }
    }
    return sumBox
}