/*function solution(num){
    let solution = {
        count : 0,
        divideNum(){
            num = num/2
            this.count += 1
            },
        sum(){
            num = num*3+1
            this.count += 1
    }
}
    if(solution['count'] == 500){
        return -1
    }else if(num == 1){
        return 0
    }else{
        do{
            if(num%2 == 0){
                solution.divideNum()
                return this;
            }else{
                solution.sum()
                return this;
            }
        }while(num == 1)
    }
}*/
function solution(num){
    let count = 0
    if(num ==1){
        return 0   
    }
    do{
        num%2==0 ? num = num/2 : num = num*3+1
        if(num == 1){
            return count + 1
        }
        count++
    }while(num != 1 && count < 500)
    return -1
}