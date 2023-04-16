function solution(n, arr1, arr2) {
    let arrF = arrToBinary(arr1 , n)
    let arrS = arrToBinary(arr2 , n)
    let answer = []
    for(let i = 0; i < arrF.length; i++){
        for(let j = 0; j< n; j++){
            answer.push(findWall(arrF[i][j], arrS[i][j]))
        }
    }
    let real = []
    do{
        real.push(answer.splice(0,n).join(''))
    }while(answer.length !== 0)
    return real
}

function arrToBinary (arr, n){
    return arr.map(item => {
        if(item.toString(2).length == n){
            return item.toString(2)
        }
        else{
            return item.toString(2).padStart(n,0)
        }
    }); 
}

function findWall (str1, str2){
    if(str1 == '1' || str2 == '1'){
        return '#'
    }
    if(str1 == '0' && str2 == '0'){
        return ' '
    }
}