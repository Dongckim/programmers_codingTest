function solution(n) {
    const numList = []
    for(let i = 1; i < n; i ++ ){
        numList.push(i)
    }
    for(let j = 0; j < numList.length; j++){
        if(n%numList[j]==1){
            return numList[j]
        }
    }
}